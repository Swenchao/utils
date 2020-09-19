import os
import threading
import time
import requests


def download(url, filename, headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3559.6 '
				  'Safari/537.36'}):
	t = DownloadWorkerThread(url, filename, headers=headers)
	t.start()
	return t


# 处理单个下载线程
class DownloadWorkerThread(threading.Thread):

	# 线程个数
	thread_count = 5

	# 线程文件锁
	file_lock = threading.Lock()
	fileinfo_lock = threading.Lock()

	def __init__(self, url, filename, headers={}, thread_count=3):
		threading.Thread.__init__(self)
		# 存储地址
		self.filename = filename
		# 下载地址
		self.url = url
		# 临时文件
		self.fileinfo_name = filename + ".tmp"
		# 请求头
		self.headers = headers
		# 线程个数
		self.thread_count = thread_count

	def run(self):

		self.range_manager = self.read_range_file()
		print(u"开始下载... \n下载网址: " + self.url + u"\n存放文件: " + self.filename)

		if self.url.strip() == "":
			return

		# 存放线程
		th_list = []
		for i in range(self.thread_count):
			thr = threading.Thread(target=self.RangeWorker, args=(self,))
			print(u"线程启动: " + thr.getName())
			thr.setDaemon(True)
			thr.start()
			th_list.append(thr)

		for thr in th_list:
			thr.join()

	# 下载文件写入
	def write_content(self, content, content_range):

		# 获得资源加锁
		self.file_lock.acquire()

		# 下载写入
		with open(self.filename, 'rb+') as f:
			f.seek(content_range[0])
			f.write(content)

		self.file_lock.release()

		self.fileinfo_lock.acquire()

		# 修改下载情况
		self.range_manager.set_written_range(content_range)

		self.fileinfo_lock.release()

	# 加锁获取文件剩余大小
	def read_next_range(self):

		# 加文件锁
		self.fileinfo_lock.acquire()
		time.sleep(0.1)

		# 读取文件剩余大小
		r = self.range_manager.get_unwritten_range()

		# 释放锁
		self.fileinfo_lock.release()

		return r

	def read_range_file(self):

		self.fileinfo_lock.acquire()

		# 判断临时是否存在（是否是任务中断续下）
		if os.path.exists(self.fileinfo_name):
			print("读取下载文件 " + self.fileinfo_name)
			manager = DownloadWorkerThread.FileInfoManager(self.fileinfo_name, url=self.url)
			self.content_length = manager.get_total_length()
			if self.url.strip() == "":
				self.url = manager.url_in_file

		# 没有临时文件说明是首次下载，获取下载文件大小
		else:
			self.content_length = self.get_content_length()

			with open(self.filename, "wb+") as f:
				f.seek(self.content_length)

			manager = DownloadWorkerThread.FileInfoManager(self.fileinfo_name, url=self.url, filesize=self.content_length)
		self.fileinfo_lock.release()
		return manager

	# 获取下载文件大小
	def get_content_length(self):

		headers = self.headers
		headers['Range'] = "bytes=0-1"
		length = 0

		while length < 1024 * 1024 * 3:

			time.sleep(3)

			# length = long(requests.get(self.url, headers=self.headers).headers['content-Range'].split('/')[1])  #

			# py3中已经没有了long类型
			length = requests.get(self.url, headers=self.headers).headers['content-Range'].split('/')[1]

			# 获取下载文件的大小
			print("文件大小：" + str(length) + " bytes")
		return length

	def RangeWorker(self, downloadWorker):

		while True:
			# 获取为下载
			content_range = downloadWorker.read_next_range()

			# 未下载为0，下载完成
			if content_range == 0:

				# 移除临时文件
				os.remove(self.fileinfo_name)
				print("下载完成")
				break

			headers = downloadWorker.headers
			headers['Range'] = "bytes=" + str(content_range[0]) + "-" + str(content_range[1] - 1)

			while True:
				iTryTimes = 0
				r = requests.get(downloadWorker.url, headers=headers)

				# 判断是否请求成功（是否有线程冲突）
				if r.ok:

					# 请求成功，写入
					downloadWorker.write_content(r.content, content_range)

					print("正在下载: " + str(round(1.0 * content_range[1] / self.content_length * 100, 2)) + "%  " + str(
						round(1.0 * content_range[1] / 1024.0 / 1024.0, 3)) + "MB" + " / " + str(
						round(self.content_length / 1024.0 / 1024.0, 2)) + "MB.")
					break
				else:
					iTryTimes += 1
					if iTryTimes > 1:
						print("Downloading " + downloadWorker.url + " error. Now Exit Thread.")
						return

	'''--------------------------------------------- 文件操作 ----------------------------------------------------'''

	# 对文件各种操作
	class FileInfoManager():

		url_in_file = ""

		# 正在下载区间
		writing_range = []

		# 已下载区间
		written_range = []

		# 未下载区间
		unwritten_range = []

		def __init__(self, filename, url="", filesize=0):
			
			self.filename = filename
			
			# 判断是不是第一次写入临时文件，如果不是则说明上次有未下载完成中断任务，会继续下载
			if not os.path.exists(filename):
				with open(filename, "w") as f:
					f.write("unwritten_range=[(0," + str(filesize) + ")]\r\n")
					f.write("writing_range=[]\r\n")
					f.write("written_range=[]\r\n")
					f.write("url_in_file=" + url)

				# 初始化只有未下载的
				self.unwritten_range.append((0, filesize))
				self.url_in_file = url

			else:
				with open(filename, "r") as f:
					for line in f.readlines():
						line = line.strip()
						if line == '':
							continue
						else:
							# 分别取出判别区间内容
							type = line.split("=")[0]

							# 上次正在下载的，改写为下载完成
							if type == "writing_range":
								type = "unwritten_range"

							elif type == "url_in_file":

								# 如果是中断续下，则恢复url
								if url.strip() == "":
									self.url_in_file = line.split("=")[1]
								# 否则设置url
								else:
									self.url_in_file = url

								continue

							for tup in line.split("=")[1][1:-2].split('),'):
								if tup.find("(") != 0:
									tup = tup[tup.find("("):]
								getattr(self, type).append((tup.split(",")[0][1:], tup.split(",")[1]))

		# 获得下载大小
		def get_total_length(self):

			# 未下载
			if len(self.unwritten_range) > 0:
				print(self.unwritten_range[-1][1])
				return self.unwritten_range[-1][1]

			# 正在下载
			elif len(self.writing_range) > 0:
				print(self.writing_range[-1][1])
				return self.writing_range[-1][1]

			# 已经下载完成
			elif len(self.written_range) > 0:
				print(self.written_range[-1][1])
				return self.written_range[-1][1]

			return 0

		# 将下载进度保存到临时文件
		def _save_to_file(self):
			with open(self.filename, "w") as f:
				f.write("writing_range=" + str(self.writing_range) + "\r\n")
				f.write("unwritten_range=" + str(self.unwritten_range) + "\r\n")
				f.write("written_range=" + str(self.written_range) + "\r\n")
				f.write("url_in_file=" + self.url_in_file)

		# 拼接任务列表（拼接未下载区间）
		def _splice(self, intervals, newInterval):
			if len(intervals) == 0:
				return []
			intervals = self._concat(intervals, (0, 0))
			response = []
			for interval in intervals:
				if interval[0] == interval[1]:
					continue
				# 区间右数字大于新区间左数字，则将区间加进来，准备拼接
				if interval[0] > newInterval[1]:
					response.append(interval)

				# 区间左数字小于新区间左数字，则将区间加进来，准备拼接
				elif interval[1] < newInterval[0]:
					response.append(interval)
				else:
					max_range = (min(interval[0], newInterval[0]), max(interval[1], newInterval[1]))  #

					# 其他情况进行比较，选出区间左右数字
					if max_range != newInterval:  # 若比较后与新区间不同，则合区间
						left = (min(max_range[0], newInterval[0]), max(max_range[0], newInterval[0]))
						right = (min(max_range[1], newInterval[1]), max(max_range[1], newInterval[1]))
						if left[0] != left[1]:  # 判断左右是否相同（先加左后加右）  若相等则说明之前已经存在不需要再加
							response.append(left)
						if right[0] != right[1]:
							response.append(right)
			return response

		# 拼接任务列表（拼接正在下载区间）
		def _concat(self, intervals, newInterval):
			if len(intervals) == 0:
				return [newInterval]
			response = [newInterval]
			for interval in intervals:

				# 取出最后一个元素
				i = response.pop()

				# 相等忽略一个
				if interval[0] == interval[1]:
					continue

				# 谁小先接谁
				if i[0] > interval[1]:
					response.append(interval)
					response.append(i)
				elif i[1] < interval[0]:
					response.append(i)
					response.append(interval)
				else:
					response.append((min(i[0], interval[0]), max(i[1], interval[1])))
			return response

		def get_unwritten_range(self, size=1024 * 1024):

			# 看是否有未下载的
			if len(self.unwritten_range) == 0:
				return 0

			# 取出第一个元素准备进行新一轮拼接
			r = self.unwritten_range[0]

			# 判断大小，进行拆分（1024*1024——1m,通过加1m来判断）
			r = (r[0], min(r[0] + size, r[1]))

			# 未下载区间
			self.unwritten_range = self._splice(self.unwritten_range, r)

			# 正在下载区间
			self.writing_range = self._concat(self.writing_range, r)
			self._save_to_file()
			return r

		# 更改下载情况
		def set_written_range(self, content_range):
			self.writing_range = self._splice(self.writing_range, content_range)
			self.written_range = self._concat(self.written_range, content_range)
			self.written_range = self._concat(self.written_range, content_range)
			self._save_to_file()

if __name__ == '__main__':

	# 下载文件地址
	url_file = ""

	# 下载到本地地址
	url_dir = ""

	t = download(url_file, url_dir)

	# 多线程
	while t.is_alive():
		time.sleep(60)

	print("最新镜像文件下载成功")