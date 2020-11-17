import pymysql.cursors


class Mysql:

    # Python连接到 MySQL 及相关操作
    connected = False
    __conn = None

    # 构造函数，初始化时直接连接数据库
    def __init__(self, conf):
        if type(conf) is not dict:
            print('错误: 参数不是字典类型！')
        else:
            # mysql连接 端口 用户名 密码 数据库
            for key in ['host', 'port', 'user', 'pw', 'db']:
                if key not in conf.keys():
                    print('错误: 参数字典缺少 %s' % key)
            # 编码
            if 'charset' not in conf.keys():
                conf['charset'] = 'utf8'
        try:
            self.__conn = pymysql.connect(
                host = conf['host'],
                port = conf['port'],
                user = conf['user'],
                passwd = conf['pw'],
                db = conf['db'],
                cursorclass = pymysql.cursors.DictCursor)
            # 修改连接状态
            self.connected = True
        except pymysql.Error as e:
            print('数据库连接失败:', end='')

    # 插入数据到数据表(字典类型传值 {'id':1, 'name':'zhangsan'} )
    def insert(self, table, val_obj):
        sql_top = 'INSERT INTO ' + table + ' ('
        sql_tail = ') VALUES ('
        try:
            for key, val in val_obj.items():
                sql_top += key + ','
                sql_tail += val + ','
            sql = sql_top[:-1] + sql_tail[:-1] + ')'
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return self.__conn.insert_id()
        except pymysql.Error as e:
            self.__conn.rollback()
            return False

    # 更新数据到数据表(传值跟新增类似)
    def update(self, table, val_obj, range_str):
        sql = 'UPDATE ' + table + ' SET '
        try:
            for key, val in val_obj.items():
                sql += key + '=' + val + ','
            sql = sql[:-1] + ' WHERE ' + range_str
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.rowcount
        except pymysql.Error as e:
            self.__conn.rollback()
            return False

    # 删除数据在数据表中
    # 表名 条件(where以后部分)
    def delete(self, table, range_str):
        sql = 'DELETE FROM ' + table + ' WHERE ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.rowcount
        except pymysql.Error as e:
            self.__conn.rollback()
            return False

    # 查询唯一数据在数据表中
    def select_one(self, table, factor_str, field='*'):
        sql = 'SELECT ' + field + ' FROM ' + table + ' WHERE ' + factor_str
        # print(sql)
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            # print(cursor.fetchall()[0])
            res = cursor.fetchall()
            # print(type(res))
            if isinstance(res, tuple):
                return False
            return res[0]
        except pymysql.Error as e:
            return False

    # 查询多条数据在数据表中
    def select_more(self, table, range_str, field='*'):
        sql = 'SELECT ' + field + ' FROM ' + table + ' WHERE ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()
        except pymysql.Error as e:
            return False

    # 统计某表某条件下的总行数
    def count(self, table, range_str='1'):
        sql = 'SELECT count(*)res FROM ' + table + ' WHERE ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()[0]['res']
        except pymysql.Error as e:
            return False

    # 统计某字段（或字段计算公式）的合计值
    def sum(self, table, field, range_str='1'):
        sql = 'SELECT SUM(' + field + ') AS res FROM ' + table + ' WHERE ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()[0]['res']
        except pymysql.Error as e:
            return False

    # 销毁对象时关闭数据库连接
    def __del__(self):
        try:
            # 关闭连接
            self.__conn.close()
        except pymysql.Error as e:
            pass

    # 关闭数据库连接
    def close(self):
        self.__del__()