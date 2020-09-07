import xlwt

excel_data = []


# 写入excel数据
def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet

    # 将数据写入第 i 行，第 j 列
    i = 0
    for data in excel_data:
        for j in range(len(data)):
            sheet1.write(i, j, data[j])
        i = i + 1

    f.save("text_data.xls")  # 保存文件


# 递归获取对应value
def pick_text(json_data, text_key, results=[]):
    # 嵌套数据的格式为dict
    if isinstance(json_data, dict):
        # 循环获取key
        for key in json_data.keys():
            data = json_data[key]
            # 继续迭代取值
            pick_text(data, text_key, results=results)
            # 当前key与目标key相同，取出数据
            if key == text_key:
                id_data = json_data['text_id']
                sole_data = []
                sole_data.append(id_data)
                sole_data.append(data)
                excel_data.append(sole_data)
                results.append(data)
    # 输入数据格式为list或者tuple
    elif isinstance(json_data, list) or isinstance(json_data, tuple):
        # 循环
        for data in json_data:
            # 迭代取值
            pick_text(data, text_key, play_id, results=results)


if __name__ == '__main__':
    data = []
    info13 = {
        "status": 0,
        "mesg": "success",
        "data": {
            "start_node_id": 214,
            "nodes_data": [
            {
                "node_reply": {
                    "text_id": None,
                    "text": None
                },
                "internal_intent_list": [],
                "internal_slot_list": [],
                "label_id": None,
                "child_node_jump_list": [
                    {
                        "condition_type": None,
                        "condition_value": {
                            "id": None,
                            "name": None
                        },
                        "child_condition": {
                            "id": None,
                            "name": None
                        },
                        "jump_to": {
                            "id": 215,
                            "name": "互动",
                            "node_type_name": "clarify",
                            "play_id": 13
                        }
                    }
                ],
                "unrecognized_reply": [
                    {
                        "text_id": None,
                        "text": None
                    }
                ],
                "node_name": "开始",
                "max_round_reply": {
                    "text_id": None,
                    "text": None
                },
                "max_stay_round": 0,
                "node_id": 214,
                "label_value_id": None,
                "label_value": None,
                "node_type": "start",
                "label": None,
                "use_faq": False,
                "faq_depository_ids": [],
                "faq_max_round": 0,
                "faq_exit_node_id": None,
                "unrecognized_node_id": None,
                "silent_node_id": None
            },
            {
                "node_reply": {
                    "text_id": 521,
                    "text": "我在"
                },
                "internal_intent_list": [
                    {
                        "intent_id": 1,
                        "intent_name": "自我介绍",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "我是由汕头市政府联合搜狗公司首创的城市虚拟形象代言人，您可以叫我“闻程同学”。闻程，寓意“闻鸡起舞日夜兼程”，代表了潮汕精神。今天我会全程陪同您一起参观，在不同区域给您介绍具体的事件和项目情况，并且会在最后的创新发展区域的不同场景给您提供智能互动体验。马上您会观看潮汕文化风貌的展示视频，欢迎和我一起体验潮汕文化！",
                            "text_id": 543
                        },
                        "is_add_round": False
                    },
                    {
                        "intent_id": 2,
                        "intent_name": "作用",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "今天我作为汕头城市虚拟形象代言人，会从潮汕文化、特区建设、产业发展等维度具体给您介绍汕头这座城市，而且会全程陪同您参观和感受，希望您也能和我一样喜爱汕头！",
                            "text_id": 544
                        },
                        "is_add_round": False
                    },
                    {
                        "intent_id": 5,
                        "intent_name": "位置",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "您现在在广东汕头城市发展与产业展示厅的潮汕文化展示区，您继续向右前方可以进入特区大事记展区。另外成果愿景、规划亮点、重点产业、创新发展几个展区欢迎您继续参观，我会在不同区域出现为您做具体介绍",
                            "text_id": 261
                        },
                        "is_add_round": False
                    },
                    {
                        "intent_id": 3,
                        "intent_name": "夸奖",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "谢谢您的鼓励，我会继续努力的。",
                            "text_id": 264
                        },
                        "is_add_round": False
                    },
                    {
                        "intent_id": 4,
                        "intent_name": "批评",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "非常抱歉，给您带来不好的体验，我会加强学习。",
                            "text_id": 263
                        },
                        "is_add_round": False
                    }
                ],
                "internal_slot_list": [
                    {
                        "slot_id": 8,
                        "slot_name": "展厅-问作用",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "今天我作为汕头城市虚拟形象代言人，会从潮汕文化、特区建设、产业发展等维度具体给您介绍汕头这座城市，而且会全程陪同您参观和感受，希望您也能和我一样喜爱汕头！",
                            "text_id": 544
                        },
                        "is_add_round": False
                    },
                    {
                        "slot_id": 6,
                        "slot_name": "展厅-自我介绍",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "我是由汕头市政府联合搜狗公司首创的城市虚拟形象代言人，您可以叫我“闻程同学”。闻程，寓意“闻鸡起舞日夜兼程”，代表了潮汕精神。",
                            "text_id": 542
                        },
                        "is_add_round": False
                    },
                    {
                        "slot_id": 7,
                        "slot_name": "展厅-问地点",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "您现在在广东汕头城市发展与产业展示厅的潮汕文化展示区，您继续向右前方可以进入特区大事记展区。另外成果愿景、规划亮点、重点产业、创新发展几个展区欢迎您继续参观，我会在不同区域出现为您做具体介绍",
                            "text_id": 261
                        },
                        "is_add_round": False
                    },
                    {
                        "slot_id": 10,
                        "slot_name": "展厅-夸奖",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "谢谢您的鼓励，我会继续努力的。",
                            "text_id": 264
                        },
                        "is_add_round": False
                    },
                    {
                        "slot_id": 9,
                        "slot_name": "展厅-批评",
                        "use_custom_reply": True,
                        "custom_reply": {
                            "text": "非常抱歉，给您带来不好的体验，我会加强学习。",
                            "text_id": 263
                        },
                        "is_add_round": False
                    }
                ],
                "label_id": None,
                "child_node_jump_list": [
                    {
                        "condition_type": "slot",
                        "condition_value": {
                            "id": 72,
                            "name": "要求结束"
                        },
                        "child_condition": {
                            "id": 72,
                            "name": "要求结束"
                        },
                        "jump_to": {
                            "id": 217,
                            "name": "结束引导",
                            "node_type_name": "end",
                            "play_id": 13
                        }
                    }
                ],
                "unrecognized_reply": [
                    {
                        "text_id": 195,
                        "text": "很抱歉，闻程没有听清楚，您可以再说一次吗？"
                    },
                    {
                        "text_id": 270,
                        "text": "闻程刚才开小差啦，您可以再说一次吗？"
                    }
                ],
                "node_name": "互动",
                "max_round_reply": {
                    "text_id": 267,
                    "text": "非常抱歉，我还没有学到这部分内容，我会加快学习进度。"
                },
                "max_stay_round": 3,
                "node_id": 215,
                "label_value_id": None,
                "label_value": None,
                "node_type": "clarify",
                "label": None,
                "use_faq": False,
                "faq_depository_ids": [],
                "faq_max_round": 0,
                "faq_exit_node_id": None,
                "unrecognized_node_id": None,
                "silent_node_id": None
            },
            {
                "node_reply": {
                    "text_id": 265,
                    "text": "您可以自由参观，有需要再唤醒我。"
                },
                "internal_intent_list": [],
                "internal_slot_list": [],
                "label_id": None,
                "child_node_jump_list": [],
                "unrecognized_reply": [
                    {
                        "text_id": None,
                        "text": None
                    }
                ],
                "node_name": "结束引导",
                "max_round_reply": {
                    "text_id": None,
                    "text": None
                },
                "max_stay_round": 0,
                "node_id": 217,
                "label_value_id": None,
                "label_value": None,
                "node_type": "end",
                "label": None,
                "use_faq": False,
                "faq_depository_ids": [],
                "faq_max_round": 0,
                "faq_exit_node_id": None,
                "unrecognized_node_id": None,
                "silent_node_id": None
            }
        ],
            "play_name": "展厅-潮汕文化（词槽及意图）",
            "play_id": 13,
            "play_description": "1",
            "placeholders": [
            [
                "#person_name#",
                "用户姓名"
            ],
            [
                "#gender#",
                "用户性别"
            ],
            [
                "#birth_date#",
                "出生日期"
            ],
            [
                "#id_card#",
                "身份证后四位"
            ],
            [
                "#bank_card#",
                "银行卡后四位"
            ],
            [
                "#loan_amount#",
                "贷款金额"
            ],
            [
                "#loan_usage#",
                "贷款用途"
            ]
        ],
            "information": {
                "repayment_channel": "",
                "organization_name": ""
            },
            "advanced_configs": {}
        },
        "utime": "2020-09-02-21-19-04"
    }
    data.append(info13)
    info16 = {
        "status": 0,
        "mesg": "success",
        "data": {
            "start_node_id": 300,
            "nodes_data": [
                {
                    "node_reply": {
                        "text_id": None,
                        "text": None
                    },
                    "internal_intent_list": [],
                    "internal_slot_list": [],
                    "label_id": None,
                    "child_node_jump_list": [
                        {
                            "condition_type": None,
                            "condition_value": {
                                "id": None,
                                "name": None
                            },
                            "child_condition": {
                                "id": None,
                                "name": None
                            },
                            "jump_to": {
                                "id": 301,
                                "name": "主动互动",
                                "node_type_name": "clarify",
                                "play_id": 16
                            }
                        }
                    ],
                    "unrecognized_reply": [
                        {
                            "text_id": None,
                            "text": None
                        }
                    ],
                    "node_name": "开始",
                    "max_round_reply": {
                        "text_id": None,
                        "text": None
                    },
                    "max_stay_round": 0,
                    "node_id": 300,
                    "label_value_id": None,
                    "label_value": None,
                    "node_type": "start",
                    "label": None,
                    "use_faq": False,
                    "faq_depository_ids": [],
                    "faq_max_round": 0,
                    "faq_exit_node_id": None,
                    "unrecognized_node_id": None,
                    "silent_node_id": None
                },
                {
                    "node_reply": {
                        "text_id": 520,
                        "text": "我在，您可以提问，例如，1980年，发生了什么大事件？我就能为您做具体介绍。"
                    },
                    "internal_intent_list": [
                        {
                            "intent_id": 1,
                            "intent_name": "自我介绍",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "我是由汕头市政府联合搜狗公司首创的城市虚拟形象代言人，您可以叫我“闻程同学”。闻程，寓意“闻鸡起舞日夜兼程”，代表了潮汕精神。",
                                "text_id": 533
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 2,
                            "intent_name": "作用",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "我可以为您介绍汕头特区发展40周年多个里程碑大事记，您可以提问，例如，1980年，发生了什么大事件？",
                                "text_id": 289
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 3,
                            "intent_name": "夸奖",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "谢谢您的鼓励，我会继续努力的。",
                                "text_id": 299
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 4,
                            "intent_name": "批评",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "非常抱歉，给您带来不好的体验，我会加强学习。",
                                "text_id": 300
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 5,
                            "intent_name": "位置",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "我们目前在“特区大事记”展区，此展区是以时间为线索，为您展示汕头特区发展40周年多个里程碑大事记。",
                                "text_id": 301
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 6,
                            "intent_name": "1980年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1980年是特区初创阶段，在1980年8月，全国人大常委会批准《广东省经济特区条例》，同意在深圳、珠海、汕头三市设置经济特区。",
                                "text_id": 275
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 7,
                            "intent_name": "1981年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1981年是特区初创阶段，这一年发生了三件重要事件。 第一件是1981年10月，中共中央、国务院批准同意在汕头设立经济特区，范围1.6平方公里。 第二件是1981年11月，汕头经济特区管理委员会正式成立。 第三件是1981年8月，国务院批准成立汕头大学。",
                                "text_id": 284
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 8,
                            "intent_name": "1983年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1983年是在特区初创阶段，汕头经济特区发展总公司与泰国正大公司签订投资合同。正大康地汕头有限公司成为汕头经济特区首家外资企业。",
                                "text_id": 277
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 9,
                            "intent_name": "1984年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1984年是在三次扩围阶段，这一年有两件重要的大事。首先是1984年11月，汕头经济特区首次扩围至52.6平方公里，分龙湖和广澳两个片区。 另外在1984年，汕头经济特区采用“三三四”“二二六”“二八”等方式，在全国创造了独一无二的补贴出售住宅解困新模式。",
                                "text_id": 547
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 10,
                            "intent_name": "1985年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1985年，中外合资企业汕头超声印制板有限公司成立，并于1988年和1991年连续两次获得全国行业仅有的质量评比一等奖。",
                                "text_id": 291
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 11,
                            "intent_name": "1987年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1987年4月，汕头经济特区在全国率先实行政府机关对企业服务的“24小时答复”承诺制度。",
                                "text_id": 292
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 12,
                            "intent_name": "1990年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1990年，汕樟机械厂成功研发生产出我国第一台凹版印刷机。1996年又成功设计研发了我国第一台智能化、自动化的凹版印刷机。",
                                "text_id": 293
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 13,
                            "intent_name": "1991年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1991年4月，汕头经济特区第二次扩围至整个汕头市区，面积为234平方公里。 同年，汕头经济特区第一家外资银行华侨商业银行汕头分行成立。",
                                "text_id": 294
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 14,
                            "intent_name": "1997年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1997年10月1日起，全国首部保护华侨房地产权益的地方性法规《汕头经济特区华侨房地产权益保护办法》实施。",
                                "text_id": 295
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 15,
                            "intent_name": "2000年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2000年5月1日起，全国首部规范个人独资企业的地方性法规《汕头经济特区个人独资企业条例》实施。",
                                "text_id": 296
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 16,
                            "intent_name": "2003年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2003年1月29日，国务院批准调整汕头市行政区划后，汕头市包括汕头市中心城区（金平、龙湖、濠江），潮阳市改设的潮阳区、潮南区，澄海市改设的澄海区，以及南澳县共6区1县。",
                                "text_id": 531
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 17,
                            "intent_name": "2011年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2011年5月，汕头经济特区第三次扩围至全市，面积2064.4平方公里。同时汕头市政府与中国交建签订汕头东海岸新城项目投资建设合同。汕头东海岸新城是汕头市政府与中国交建进行战略合作的大型城市综合运营项目。",
                                "text_id": 297
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 18,
                            "intent_name": "2013年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2013年8月1日起，全国首部预防腐败的地方性法规《汕头经济特区预防腐败条例》实施。",
                                "text_id": 298
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 19,
                            "intent_name": "2014年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2014年9月，国务院批复同意在汕头经济特区设立华侨经济文化合作试验区。华侨经济文化合作试验区处于汕头经济特区核心地带，区位条件优越，优势突出，具备加快发展的条件和潜力。",
                                "text_id": 278
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 20,
                            "intent_name": "2016年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2016年12月，广东以色列理工学院获教育部批准正式设立，是由以色列理工学院与汕头大学合作创立的一所具有独立法人资格的中外合作大学。",
                                "text_id": 279
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 21,
                            "intent_name": "2017年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2017年2月，国务院批复同意汕头高新技术产业园区，升级为国家高新技术产业开发区，定名为汕头高新技术产业开发区。",
                                "text_id": 280
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 22,
                            "intent_name": "2019年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2019年3月，汕头市成功获得2021年第三届亚洲青年运动会举办权，成为国内继北京、广州、南京、杭州之后第五个获得洲际综合性运动会举办权的城市。",
                                "text_id": 281
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 23,
                            "intent_name": "2020年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2020年3月，国务院正式批复同意汕头经济特区保税区，整合优化为汕头综合保税区，成为广东省第五个、粤东首个综合保税区。 6月，广东省政府出台24条政策支持汕头华侨试验区高质量发展，这标志着汕头扬帆起航再出发",
                                "text_id": 532
                            },
                            "is_add_round": False
                        }
                    ],
                    "internal_slot_list": [
                        {
                            "slot_id": 6,
                            "slot_name": "展厅-自我介绍",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "我是由汕头市政府联合搜狗公司首创的城市虚拟形象代言人，您可以叫我“闻程同学”。闻程，寓意“闻鸡起舞日夜兼程”，代表了潮汕精神。",
                                "text_id": 533
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 7,
                            "slot_name": "展厅-问地点",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "我们目前在“特区大事记”展区，此展区是以时间为线索，为您展示汕头特区发展40周年多个里程碑大事记。",
                                "text_id": 397
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 8,
                            "slot_name": "展厅-问作用",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "您可以提问，例如，1980年，发生了什么大事件？我就能为您做具体介绍。",
                                "text_id": 370
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 9,
                            "slot_name": "展厅-批评",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "非常抱歉，给您带来不好的体验，我会加强学习。",
                                "text_id": 396
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 10,
                            "slot_name": "展厅-夸奖",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "谢谢您的鼓励，我会继续努力的。",
                                "text_id": 395
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 11,
                            "slot_name": "大事记-1980年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1980年是特区初创阶段，在1980年8月，全国人大常委会批准《广东省经济特区条例》，同意在深圳、珠海、汕头三市设置经济特区。",
                                "text_id": 371
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 12,
                            "slot_name": "大事记-1981年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1981年是特区初创阶段，这一年发生了三件重要事件。 第一件是1981年10月，中共中央、国务院批准同意在汕头设立经济特区，范围1.6平方公里。 第二件是1981年11月，汕头经济特区管理委员会正式成立。 第三件是1981年8月，国务院批准成立汕头大学。",
                                "text_id": 380
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 13,
                            "slot_name": "大事记-1983年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1983年是在特区初创阶段，汕头经济特区发展总公司与泰国正大公司签订投资合同。正大康地汕头有限公司成为汕头经济特区首家外资企业。",
                                "text_id": 373
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 14,
                            "slot_name": "大事记-2014年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2014年9月，国务院批复同意在汕头经济特区设立华侨经济文化合作试验区。华侨经济文化合作试验区处于汕头经济特区核心地带，区位条件优越，优势突出，具备加快发展的条件和潜力。",
                                "text_id": 374
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 16,
                            "slot_name": "大事记-2016年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2016年12月，广东以色列理工学院获教育部批准正式设立，是由以色列理工学院与汕头大学合作创立的一所具有独立法人资格的中外合作大学。",
                                "text_id": 375
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 17,
                            "slot_name": "大事记-2017年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2017年2月，国务院批复同意汕头高新技术产业园区，升级为国家高新技术产业开发区，定名为汕头高新技术产业开发区。",
                                "text_id": 376
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 18,
                            "slot_name": "大事记-2019年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2019年3月，汕头市成功获得2021年第三届亚洲青年运动会举办权，成为国内继北京、广州、南京、杭州之后第五个获得洲际综合性运动会举办权的城市。",
                                "text_id": 377
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 19,
                            "slot_name": "大事记-2020年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2020年3月，国务院正式批复同意汕头经济特区保税区，整合优化为汕头综合保税区，成为广东省第五个、粤东首个综合保税区。 6月，广东省政府出台24条政策支持汕头华侨试验区高质量发展，这标志着汕头扬帆起航再出发",
                                "text_id": 532
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 21,
                            "slot_name": "大事记-1984年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1984年是在三次扩围阶段，这一年有两件重要的大事。首先是1984年11月，汕头经济特区首次扩围至52.6平方公里，分龙湖和广澳两个片区。 另外在1984年，汕头经济特区采用“三三四”“二二六”“二八”等方式，在全国创造了独一无二的补贴出售住宅解困新模式。",
                                "text_id": 547
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 22,
                            "slot_name": "大事记-1985年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1985年，中外合资企业汕头超声印制板有限公司成立，并于1988年和1991年连续两次获得全国行业仅有的质量评比一等奖。",
                                "text_id": 387
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 23,
                            "slot_name": "大事记-1987年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1987年4月，汕头经济特区在全国率先实行政府机关对企业服务的“24小时答复”承诺制度。",
                                "text_id": 388
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 24,
                            "slot_name": "大事记-1990年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1990年，汕樟机械厂成功研发生产出我国第一台凹版印刷机。1996年又成功设计研发了我国第一台智能化、自动化的凹版印刷机。",
                                "text_id": 389
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 25,
                            "slot_name": "大事记-1991年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1991年4月，汕头经济特区第二次扩围至整个汕头市区，面积为234平方公里。 同年，汕头经济特区第一家外资银行华侨商业银行汕头分行成立。",
                                "text_id": 390
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 26,
                            "slot_name": "大事记-1997年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "1997年10月1日起，全国首部保护华侨房地产权益的地方性法规《汕头经济特区华侨房地产权益保护办法》实施。",
                                "text_id": 391
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 27,
                            "slot_name": "大事记-2000年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2000年5月1日起，全国首部规范个人独资企业的地方性法规《汕头经济特区个人独资企业条例》实施。",
                                "text_id": 392
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 28,
                            "slot_name": "大事记-2011年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2011年5月，汕头经济特区第三次扩围至全市，面积2064.4平方公里。同时汕头市政府与中国交建签订汕头东海岸新城项目投资建设合同。汕头东海岸新城是汕头市政府与中国交建进行战略合作的大型城市综合运营项目。",
                                "text_id": 393
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 29,
                            "slot_name": "大事记-2013年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2013年8月1日起，全国首部预防腐败的地方性法规《汕头经济特区预防腐败条例》实施。",
                                "text_id": 394
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 80,
                            "slot_name": "大事记-2003年",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "2003年1月29日，国务院批准调整汕头市行政区划后，汕头市包括汕头市中心城区（金平、龙湖、濠江），潮阳市改设的潮阳区、潮南区，澄海市改设的澄海区，以及南澳县共6区1县。",
                                "text_id": 531
                            },
                            "is_add_round": False
                        }
                    ],
                    "label_id": None,
                    "child_node_jump_list": [
                        {
                            "condition_type": "slot",
                            "condition_value": {
                                "id": 72,
                                "name": "要求结束"
                            },
                            "child_condition": {
                                "id": 72,
                                "name": "要求结束"
                            },
                            "jump_to": {
                                "id": 329,
                                "name": "结束",
                                "node_type_name": "end",
                                "play_id": 16
                            }
                        }
                    ],
                    "unrecognized_reply": [
                        {
                            "text_id": 382,
                            "text": "闻程刚才开小差啦，您可以再说一次吗？"
                        },
                        {
                            "text_id": 381,
                            "text": "很抱歉，闻程没有听清楚，您可以再说一次吗？"
                        }
                    ],
                    "node_name": "主动互动",
                    "max_round_reply": {
                        "text_id": 383,
                        "text": "这个问题闻程还在学习中，让闻程为您介绍一下2019年的大事件吧：2019年3月，汕头市成功获得2021年第三届亚洲青年运动会举办权，成为国内继北京、广州、南京、杭州之后第五个获得洲际综合性运动会举办权的城市。"
                    },
                    "max_stay_round": 3,
                    "node_id": 301,
                    "label_value_id": None,
                    "label_value": None,
                    "node_type": "clarify",
                    "label": None,
                    "use_faq": False,
                    "faq_depository_ids": [],
                    "faq_max_round": 0,
                    "faq_exit_node_id": None,
                    "unrecognized_node_id": None,
                    "silent_node_id": None
                },
                {
                    "node_reply": {
                        "text_id": 401,
                        "text": "您可以自由参观，有需要再唤醒我。"
                    },
                    "internal_intent_list": [],
                    "internal_slot_list": [],
                    "label_id": None,
                    "child_node_jump_list": [],
                    "unrecognized_reply": [
                        {
                            "text_id": None,
                            "text": None
                        }
                    ],
                    "node_name": "结束",
                    "max_round_reply": {
                        "text_id": None,
                        "text": None
                    },
                    "max_stay_round": 0,
                    "node_id": 329,
                    "label_value_id": None,
                    "label_value": None,
                    "node_type": "end",
                    "label": None,
                    "use_faq": False,
                    "faq_depository_ids": [],
                    "faq_max_round": 0,
                    "faq_exit_node_id": None,
                    "unrecognized_node_id": None,
                    "silent_node_id": None
                }
            ],
            "play_name": "展厅-大事记展区（意图）",
            "play_id": 16,
            "play_description": "2",
            "placeholders": [
                [
                    "#person_name#",
                    "用户姓名"
                ],
                [
                    "#gender#",
                    "用户性别"
                ],
                [
                    "#birth_date#",
                    "出生日期"
                ],
                [
                    "#id_card#",
                    "身份证后四位"
                ],
                [
                    "#bank_card#",
                    "银行卡后四位"
                ],
                [
                    "#loan_amount#",
                    "贷款金额"
                ],
                [
                    "#loan_usage#",
                    "贷款用途"
                ]
            ],
            "information": {
                "repayment_channel": "",
                "organization_name": ""
            },
            "advanced_configs": {}
        },
        "utime": "2020-09-03-06-13-28"
    }
    data.append(info16)
    info18 = {
        "status": 0,
        "mesg": "success",
        "data": {
            "start_node_id": 347,
            "nodes_data": [
                {
                    "node_reply": {
                        "text_id": None,
                        "text": None
                    },
                    "internal_intent_list": [],
                    "internal_slot_list": [],
                    "label_id": None,
                    "child_node_jump_list": [
                        {
                            "condition_type": None,
                            "condition_value": {
                                "id": None,
                                "name": None
                            },
                            "child_condition": {
                                "id": None,
                                "name": None
                            },
                            "jump_to": {
                                "id": 348,
                                "name": "互动",
                                "node_type_name": "clarify",
                                "play_id": 18
                            }
                        }
                    ],
                    "unrecognized_reply": [
                        {
                            "text_id": None,
                            "text": None
                        }
                    ],
                    "node_name": "开始",
                    "max_round_reply": {
                        "text_id": None,
                        "text": None
                    },
                    "max_stay_round": 0,
                    "node_id": 347,
                    "label_value_id": None,
                    "label_value": None,
                    "node_type": "start",
                    "label": None,
                    "use_faq": False,
                    "faq_depository_ids": [],
                    "faq_max_round": 0,
                    "faq_exit_node_id": None,
                    "unrecognized_node_id": None,
                    "silent_node_id": None
                },
                {
                    "node_reply": {
                        "text_id": 517,
                        "text": "我在"
                    },
                    "internal_intent_list": [
                        {
                            "intent_id": 1,
                            "intent_name": "自我介绍",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "我是由汕头市政府联合搜狗公司首创的城市虚拟形象代言人，您可以叫我“闻程同学”。闻程，寓意“闻鸡起舞日夜兼程”，代表了潮汕精神。",
                                "text_id": 534
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 2,
                            "intent_name": "作用",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "您可以说出您感兴趣的内容，例如，亚青会的项目数或者“珠港新城“项目名称，我就可以为您解答了。",
                                "text_id": 446
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 3,
                            "intent_name": "夸奖",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "谢谢您的鼓励，我会继续努力的。",
                                "text_id": 438
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 4,
                            "intent_name": "批评",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "非常抱歉，给您带来不好的体验，我会加强学习。",
                                "text_id": 437
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 5,
                            "intent_name": "位置",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "您现在在沙盘展示区，本展区展示了华侨经济合作实验区的32个重点项目展项和亚青会相关情况。",
                                "text_id": 498
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 24,
                            "intent_name": "亚青会全称是什么？",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会的全称是亚洲青年运动会，简称亚青会，是亚洲规模最大的青年综合性运动会，由亚洲奥林匹克理事会的成员国轮流主办。国际奥林匹克委员会承认亚洲青年运动会为正式的亚洲地区青年运动会。",
                                "text_id": 480
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 25,
                            "intent_name": "亚青会多久举办一次？",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会每四年举办一届，自2009年开始第1届，2017年举办了第2届，会在2021年举办第三届，举办地在中国汕头",
                                "text_id": 481
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 26,
                            "intent_name": "本次的亚青会是第几届？",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "本次汕头2021年举办的是第三届亚青会",
                                "text_id": 528
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 27,
                            "intent_name": "亚青会举办时间",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会将于2021年11月20日-2021年11月28日在中国汕头举行",
                                "text_id": 523
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 28,
                            "intent_name": "亚青会有多少个参赛地区？",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会的参赛国主要分布在东亚，东南亚，南亚，西亚，中亚，包含45个国家及地区",
                                "text_id": 529
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 29,
                            "intent_name": "亚青会会徽是什么？",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会最新版会徽于2006年12月2日在多哈亚运会期间公布，中央是红日，红日上面盘环绕着一条龙，下面环绕着一只鹰，代表亚洲的团结，并强调了东方巨龙中国以及鹰所代表的阿拉伯国家在亚洲体育中所起的重要作用。会徽下方是五环以及“Olympic Council of Asia”的字样",
                                "text_id": 524
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 30,
                            "intent_name": "亚青会有多少个项目？",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会一共有18个大项：田径；水上运动包含游泳、跳水、水球；羽毛球；3*3篮球；沙滩排球；龙舟；足球；体操；高尔夫；手球；街舞；攀岩；橄榄球；冲浪；乒乓球；跆拳道；帆板和武术",
                                "text_id": 530
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 31,
                            "intent_name": "亚青会组织建设进度怎样？",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会组织建设，是自2019年3月3日亚青会申办成功以来，汕头充分调动全市力量投入到这项工作当中。5月18日成立筹备工作领导小组，下设办公室，由分管市领导具体抓日常工作，2020年成立执委会，已开始分期分批从全市选调人员，全脱产参加执委会工作，执委会下设办公室、竞赛部、场馆建设部、文化交流部、外联部等16个部门。",
                                "text_id": 527
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 32,
                            "intent_name": "场馆建设情况？",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "本次汕头亚青会会场馆建设是按照“节俭办赛”原则，汕头充分利用现有场馆设施，在建设阶段就充分考虑场馆的赛后利用。场馆建设主要分两部分： 第一，新建两个场馆。一个是作为举办开幕式和田径、体操比赛的亚青会主场馆，另一个是承担大量比赛项目的体育运动产业基地，是结合新体校建设，在原来的游泳跳水馆基础上进行扩建。 第二，改造升级20个现有场馆，目前大部分项目已完成立项，开始维修改造，今年底前完成改造11个，剩余9个项目最迟于明年3月投入使用。这部分场馆赛后将作为学校教学、重要文体活动场所和全民运动健身、省级体育赛事等活动场所。",
                                "text_id": 525
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 33,
                            "intent_name": "亚青会的整体统筹和竞赛组织情况？",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "本次汕头亚青会按照举办时间2021年，倒排工作周期，聘请国家级专家顾问，制定总体策划方案，明晰时间表、路线图，按照规划、准备、运行、总结四个阶段，梳理出92项重要任务节点。 推进信息化建设，着力打造“智慧亚青”。开展亚青会信息技术与通信系统规划编制，目前已完成规划初稿。推动场馆建设与信息化建设同步实施，充分运用5G、人工智能、4K/8K等新一代信息技术，提升场馆信息化水平。",
                                "text_id": 526
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 34,
                            "intent_name": "雅士利天澜国际大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "雅士利·天澜国际大厦项目位于珠港新城总部经济园区，总占地面积15.2亩，总建筑面积7.44万平方米，总投资4.8亿元。项目东塔26层，西塔24层，配备3层大型地下停车场，是集商务金融办公、商业、公寓于一体的新型城市综合体。项目于2017年12月竣工验收并投入使用",
                                "text_id": 535
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 35,
                            "intent_name": "联泰时代总部中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "联泰时代总部中心项目位于珠港新城总部经济园区，总占地面积48.5亩，总建筑面积10万平方米，总投资6.81亿元。项目建设1栋19层联泰总部办公大楼、1栋17层公寓楼、1栋8层和1幢11层创意办公室。项目将于2020年12月竣工验收并投入使用",
                                "text_id": 536
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 36,
                            "intent_name": "广东航宇卫星大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "广东航宇卫星大厦位于珠港新城总部经济园区，总占地面积12.56亩，总建筑面积1.6万平方米，总投资1亿元。航宇卫星科技有限公司是中国卫星在南方的重要基地，拥有广东省卫星应用工程技术研究开发中心、广东省博士工作站。项目于2014年1月竣工验收并投入使用。",
                                "text_id": 537
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 37,
                            "intent_name": "太安堂总部大楼",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "太安堂总部大楼项目位于珠港新城总部经济园区，总占地面积15.77亩，总建筑面积5.03万平米，总投资1.8亿元。项目集商业、办公、多种功能为一体，共24层，其中1到3层为立体商业空间，4层为空中花园，配备三层地下车库，项目于2018年12月竣工验收并投入使用。",
                                "text_id": 538
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 38,
                            "intent_name": "潮商中心大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "潮商中心大厦项目位于珠港新城总部经济园区，总占地面积60.6亩，总建筑面积约30万平方米，总投资26亿元。项目主要建设一栋5A甲级写字楼，一栋SOHO公寓，两栋酒店式公寓，配备大型集中商业，兼建造一栋独立潮会所。项目将于2022年6月竣工验收并投入使用。",
                                "text_id": 539
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 39,
                            "intent_name": "龙光世纪商务中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "龙光世纪商务中心项目位于珠港新城总部经济园区，总占地面积76.6亩，总建筑面积约23万平方米，总投资17.5亿元。项目定位为珠港新城高端商业CBD，将倾力打造成珠港新城未来极具代表性的名片级作品，为全球潮汕人敬献一座滨海商务范本。项目将于2022年1月竣工验收并投入使用。",
                                "text_id": 453
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 40,
                            "intent_name": "金东海科创中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "金东海科创中心项目位于珠港新城总部经济园区，总占地面积36.6亩，总建筑面积8.2平方米，总投资约10亿元。项目一期建设高层办公楼1栋29层、两栋28层，商业裙楼4层；二期建设高层服务型公寓两栋30层，商业裙楼4层，地下室2层，打造涵盖商务办公、科创研发、文化旅游、高端居住等多种功能于一体的粤东滨海休闲商务区。项目将于2022年1月竣工验收并投入使用",
                                "text_id": 540
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 41,
                            "intent_name": "潮金大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "潮金大厦位于珠港新城总部经济园区，总占地面积12.8亩，总建筑面积4.3万平方米，总投资1.6亿元。项目规划高层文化大楼1栋14层，多层文化大楼1栋5层，裙楼文化配套3层，包括演出剧场、写字楼及其它文化配套设施等，致力打造为集剧院、文化展示、商务于一体，融自然景观、人文风情于一体的潮剧文化艺术殿堂。项目将于2022年3月竣工验收并投入使用。",
                                "text_id": 455
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 42,
                            "intent_name": "国瑞会展中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "国瑞会展中心位于汕头珠港新城总部经济园区，占地约100亩，总建筑面积约35万平方米，总投资约28亿元。规划建设国瑞∙观海居、大型国际会展中心、5A甲级写字楼和万豪国际五星级酒店，是含住宅、写字楼、商业、酒店于一体的城市高端海景综合体，万豪酒店拟作为亚青会配套接待酒店。项目计划于2021年10月竣工并投入使用。",
                                "text_id": 456
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 43,
                            "intent_name": "泰盛科创园",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "泰盛科创园项目位于东海岸新城新津片区，总占地面积约251亩，总建筑面积约100万平方米，总投资65亿元。项目主要建设潮侨金融高科总部中心、潮侨创意办公基地、海湾文化中心、宝能环球汇、五星酒店、高端人才公寓及相关配套。项目将于2022年12月竣工验收并投入使用。",
                                "text_id": 457
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 44,
                            "intent_name": "明园汕头国际科创金融城",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "明园汕头国际科创金融城项目位于东海岸新城新津片区，总占地面积115亩，总建筑面积55万平方米，总投资56亿元。项目建设6栋超高层建筑，涵盖超五星级酒店、5A级办公楼、文化艺术中心、高端商业、公寓等各大业态。项目将于2022年6月竣工验收并投入使用。",
                                "text_id": 458
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 45,
                            "intent_name": "华润海湾中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "华润海湾中心项目位于东海岸新城新津片区，总占地面积120亩，总建筑面积35.85万平方米，总投资约25亿元，包含东海岸新城首个大型购物中心万象天地及高品质住宅。项目将于2023年12月竣工验收并投入使用。",
                                "text_id": 459
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 46,
                            "intent_name": "汕头大学香港中文大学联合汕头国际眼科中心易地扩建项目",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头大学·香港中文大学联合汕头国际眼科中心易地扩建项目位于东海岸新城新津片区，总占地面积20亩，总建筑面积5.7万平方米，总投资3.85亿元。项目规划床位300张，项目将于2022年12月竣工验收并投入使用。",
                                "text_id": 460
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 47,
                            "intent_name": "华侨试验区国家示范性高中和国际学校项目",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "华侨试验区国家示范性高中和国际学校项目位于东海岸新城新津片区，总占地面积135亩，总建筑面积15万平方米，总投资8.86亿元。项目将于2021年4月竣工验收并投入使用。",
                                "text_id": 461
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 48,
                            "intent_name": "汕头金中华侨试验区学校",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头金中华侨试验区学校位于东海岸新城新津片区，总占地面积66亩，总建筑面积2.8万平方米，总投资1.26亿元。现有在校生近1500人，36个教学班。",
                                "text_id": 462
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 49,
                            "intent_name": "汕头华侨试验区金湾学校",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头华侨试验区金湾学校位于东海岸新城新津片区，占地面积83.4亩，总建筑面积4.42万平方米，总投资约2.30亿元，是龙湖区政府批准设立的九年一贯制公办学校，已于2020年8月竣工并交付使用。",
                                "text_id": 463
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 50,
                            "intent_name": "津湾、东海岸公园",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "津湾、东海岸公园项目位于东海岸新城新津片区，总用地面积约625 亩，总投资约3.4亿元。其中：公园绿地397 亩，防护绿地115 亩，河涌水体75 亩，供电及社会停车场38 亩。项目将于2020年10月竣工验收并开园。",
                                "text_id": 464
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 51,
                            "intent_name": "侨韵文化旅游商业带",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头市侨韵文化旅游商业带项目位于汕头东海岸新城新溪、塔岗围片区北部主河涌两岸，总投资约13.7亿元，拟建设河涌绿地面积245.85公顷。项目将于2021年11月竣工验收并投入使用。",
                                "text_id": 465
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 52,
                            "intent_name": "汕头市东海岸新城地下综合管廊工程",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头市东海岸新城地下综合管廊工程位于东海岸新城新溪片区，总投资约18.97亿元。项目采用电力、通讯、给水、燃气管线入廊的方案，敷设干线管廊12.75 千米，过街管廊2.8 千米，是粤东地区首个城市地下综合管廊项目。项目将于2021年6月竣工验收并投入使用。",
                                "text_id": 466
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 53,
                            "intent_name": "汕头大学东校区暨亚青会场馆",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头大学东校区暨亚青会场馆项目位于东海岸新城塔岗围片区，规划总用地面积1551亩，总建筑面积约82万平方米，总投资约70亿元，分四期规划建设。一期为场馆区（“一场两馆”），二期为学生宿舍区（运动员村），一、二期计划于2021年5月底前建成；三期为教学实验区，计划于2022年6月底前建成；四期为扩容新增建设用地，计划于2024年底前建成。项目建成后可容纳2万名全日制在校生。",
                                "text_id": 467
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 54,
                            "intent_name": "汕头市中心医院易地重建项目（重大疫情救治基地）",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头市中心医院易地重建项目位于东海岸新城塔岗围片区，规划占地面积197.79亩，总建筑面积51.3万平方米，总投资约46亿元。项目设置床位3000张，建设内容包含设置国际医疗部，提供环境优越的高端医疗服务。遇重大疫情时，医院可快速转换为重症患者救治基地。项目将于2022年8月竣工验收并投入使用。",
                                "text_id": 468
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 55,
                            "intent_name": "龙湖中央商务区",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "龙湖中央商务区以高铁客运站汕头站为核心，规划面积约47平方公里，核心区面积约3.5平方公里，借助高铁枢纽客运站建设契机，整合广梅汕铁路增建二线、汕汕铁路（350高铁）、地铁、城际和轻轨等轨道交通资源，通过推动综合交通枢纽的建设带动周边片区的发展，形成城中有站，站中有城的汕头新门户和综合性城市中心。",
                                "text_id": 469
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 56,
                            "intent_name": "汕头高铁站综合交通枢纽",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头高铁站综合交通枢纽总规模11台23线，包括高铁普铁8台17线，城际铁路3台6线；计划建设10万平米的现代化高铁站房和占地6.3万平米的站前广场；预计2023年建成。汕头站将建设成为集高铁、普铁、城际铁路、城市轨道、公路客运、城市公交等多种方式于一体，便捷换乘的高质量综合交通枢纽，并以此为核心，站城融合，打造一流的中央商务区。",
                                "text_id": 470
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 57,
                            "intent_name": "新津片区",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "规划面积5.18平方公里，重点发展科技金融、休闲娱乐和高端居住产业",
                                "text_id": 471
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 58,
                            "intent_name": "新溪片区",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "规划面积11.7平方公里，重点发展数字经济、贸易会展、文化创意产业",
                                "text_id": 472
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 59,
                            "intent_name": "塔岗围片区",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "规划面积7.4平方公里，重点发展休闲旅游、科教文卫产业",
                                "text_id": 473
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 60,
                            "intent_name": "珠港新城",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "珠港新城是华侨试验区核心区和直管区的重要组成部分，规划面积3.51平方公里。重点打造粤东区域性总部乃至世界侨商潮商总部经济区，以文化传承、低碳交通、生态绿城为理念，构筑新城空间结构，高标准打造汕头总部经济区",
                                "text_id": 474
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 61,
                            "intent_name": "东海岸新城",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "东海岸新城是华侨试验区核心区和直管区的重要组成部分，规划面积24平方公里，其中陆域约20平方公里，包括津湾、溪湾、莱湾三个片区。规划定位为粤东区域综合服务中心、城市中央商务区、行政文化中心和生态型海岸新城",
                                "text_id": 475
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 62,
                            "intent_name": "华侨试验区人才大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头华侨试验区人才大厦共7层，面积5800平方米，配套党群服务中心、人才服务中心、创客办公室、68套人才公寓、多功能厅、健身房等功能区，是中共汕头市委组织部牵头华侨试验区共同打造的华侨华人、潮籍英才回国回乡创新创业“归谷”和各类人才拎包入驻的综合服务平台，加挂广东省“扬帆计划”汕头市人才驿站分站牌子。",
                                "text_id": 476
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 63,
                            "intent_name": "路网",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "珠港新城规划范围内包括5条城市主干道，分别为泰山路南延段、中山东路、海滨路东延段、天山南路、嵩山南路等；以及4条次干道，分别为珠城路、衡山路、黄山路、海兴路。东海岸新城内部三个片区通过全长16公里的“一路两桥”即东海岸大道和新津大桥、东海岸大桥连接贯通；同时三个片区分别通过13条南北向的主次干道与北侧腹地连接，形成密集的对外交通网络布局。未来东海岸新城将依托中阳大道快速路强化片区的道路网络体系。",
                                "text_id": 545
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 64,
                            "intent_name": "试验区规划建设情况",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "华侨试验区规划面积480平方公里，其中直管区规划面积28.82平方公里，包括珠港新城、东海岸新城和蓝水星片区。珠港新城3.51平方公里，产业方向以总部经济为主；东海岸新城新津片区（含蓝水星片区）6.23平方公里，产业方向以科技金融、休闲娱乐、高端商住为主；东海岸新城新溪片区11.7平方公里，产业方向以科技信息、贸易会展、文化创意为主；东海岸新城塔岗围片区7.4平方公里，产业方向以休闲旅游、科教文卫为主。目前，直管区范围内在建、已建市政道路总长约60公里，东海岸新城25公里海堤已完成，正全面推进公园绿地、综合管廊、学校、医院等基础设施和公共配套设施建设。",
                                "text_id": 478
                            },
                            "is_add_round": False
                        },
                        {
                            "intent_id": 65,
                            "intent_name": "试验区产业发展情况",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "根据国务院的批复要求和试验区产业发展定位，试验区重点发展跨境金融、商务会展、资源能源交易、文化创意、旅游休闲、教育培训、医疗服务、信息、海洋等九大都市产业。目前，试验区正着力发展金融服务业、总部经济等现代服务业和数字经济、人工智能、供应链等新产业新业态。整个直管区现有产业项目13个，总投资量约290亿元；存量登记注册企业691家，总注册资本456.87亿元",
                                "text_id": 541
                            },
                            "is_add_round": False
                        }
                    ],
                    "internal_slot_list": [
                        {
                            "slot_id": 6,
                            "slot_name": "展厅-自我介绍",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "我是由汕头市政府联合搜狗公司首创的城市虚拟形象代言人，您可以叫我“闻程同学”。闻程，寓意“闻鸡起舞日夜兼程”，代表了潮汕精神。",
                                "text_id": 534
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 7,
                            "slot_name": "展厅-问地点",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "您现在在沙盘展示区，本展区展示了华侨经济合作实验区的32个重点项目展项和亚青会相关情况。",
                                "text_id": 498
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 8,
                            "slot_name": "展厅-问作用",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "您可以说出您感兴趣的内容，例如，亚青会的项目数或者“珠港新城“项目名称，我就可以为您解答了。",
                                "text_id": 446
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 9,
                            "slot_name": "展厅-批评",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "非常抱歉，给您带来不好的体验，我会加强学习。",
                                "text_id": 437
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 10,
                            "slot_name": "展厅-夸奖",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "谢谢您的鼓励，我会继续努力的。",
                                "text_id": 438
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 30,
                            "slot_name": "雅士利·天澜国际大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "雅士利·天澜国际大厦项目位于珠港新城总部经济园区，总占地面积15.2亩，总建筑面积7.44万平方米，总投资4.8亿元。项目东塔26层，西塔24层，配备3层大型地下停车场，是集商务金融办公、商业、公寓于一体的新型城市综合体。项目于2017年12月竣工验收并投入使用",
                                "text_id": 535
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 31,
                            "slot_name": "联泰时代总部中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "联泰时代总部中心项目位于珠港新城总部经济园区，总占地面积48.5亩，总建筑面积10万平方米，总投资6.81亿元。项目建设1栋19层联泰总部办公大楼、1栋17层公寓楼、1栋8层和1幢11层创意办公室。项目将于2020年12月竣工验收并投入使用",
                                "text_id": 536
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 32,
                            "slot_name": "广东航宇卫星大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "广东航宇卫星大厦位于珠港新城总部经济园区，总占地面积12.56亩，总建筑面积1.6万平方米，总投资1亿元。航宇卫星科技有限公司是中国卫星在南方的重要基地，拥有广东省卫星应用工程技术研究开发中心、广东省博士工作站。项目于2014年1月竣工验收并投入使用。",
                                "text_id": 537
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 33,
                            "slot_name": "太安堂总部大楼",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "太安堂总部大楼项目位于珠港新城总部经济园区，总占地面积15.77亩，总建筑面积5.03万平米，总投资1.8亿元。项目集商业、办公、多种功能为一体，共24层，其中1到3层为立体商业空间，4层为空中花园，配备三层地下车库，项目于2018年12月竣工验收并投入使用。",
                                "text_id": 538
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 34,
                            "slot_name": "潮商中心大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "潮商中心大厦项目位于珠港新城总部经济园区，总占地面积60.6亩，总建筑面积约30万平方米，总投资26亿元。项目主要建设一栋5A甲级写字楼，一栋SOHO公寓，两栋酒店式公寓，配备大型集中商业，兼建造一栋独立潮会所。项目将于2022年6月竣工验收并投入使用。",
                                "text_id": 539
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 35,
                            "slot_name": "龙光世纪商务中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "龙光世纪商务中心项目位于珠港新城总部经济园区，总占地面积76.6亩，总建筑面积约23万平方米，总投资17.5亿元。项目定位为珠港新城高端商业CBD，将倾力打造成珠港新城未来极具代表性的名片级作品，为全球潮汕人敬献一座滨海商务范本。项目将于2022年1月竣工验收并投入使用。",
                                "text_id": 453
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 36,
                            "slot_name": "金东海科创中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "金东海科创中心项目位于珠港新城总部经济园区，总占地面积36.6亩，总建筑面积8.2平方米，总投资约10亿元。项目一期建设高层办公楼1栋29层、两栋28层，商业裙楼4层；二期建设高层服务型公寓两栋30层，商业裙楼4层，地下室2层，打造涵盖商务办公、科创研发、文化旅游、高端居住等多种功能于一体的粤东滨海休闲商务区。项目将于2022年1月竣工验收并投入使用",
                                "text_id": 540
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 37,
                            "slot_name": "潮金大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "潮金大厦位于珠港新城总部经济园区，总占地面积12.8亩，总建筑面积4.3万平方米，总投资1.6亿元。项目规划高层文化大楼1栋14层，多层文化大楼1栋5层，裙楼文化配套3层，包括演出剧场、写字楼及其它文化配套设施等，致力打造为集剧院、文化展示、商务于一体，融自然景观、人文风情于一体的潮剧文化艺术殿堂。项目将于2022年3月竣工验收并投入使用。",
                                "text_id": 455
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 38,
                            "slot_name": "国瑞会展中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "国瑞会展中心位于汕头珠港新城总部经济园区，占地约100亩，总建筑面积约35万平方米，总投资约28亿元。规划建设国瑞∙观海居、大型国际会展中心、5A甲级写字楼和万豪国际五星级酒店，是含住宅、写字楼、商业、酒店于一体的城市高端海景综合体，万豪酒店拟作为亚青会配套接待酒店。项目计划于2021年10月竣工并投入使用。",
                                "text_id": 456
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 39,
                            "slot_name": "泰盛科创园",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "泰盛科创园项目位于东海岸新城新津片区，总占地面积约251亩，总建筑面积约100万平方米，总投资65亿元。项目主要建设潮侨金融高科总部中心、潮侨创意办公基地、海湾文化中心、宝能环球汇、五星酒店、高端人才公寓及相关配套。项目将于2022年12月竣工验收并投入使用。",
                                "text_id": 457
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 40,
                            "slot_name": "明园汕头国际科创金融城",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "明园汕头国际科创金融城项目位于东海岸新城新津片区，总占地面积115亩，总建筑面积55万平方米，总投资56亿元。项目建设6栋超高层建筑，涵盖超五星级酒店、5A级办公楼、文化艺术中心、高端商业、公寓等各大业态。项目将于2022年6月竣工验收并投入使用。",
                                "text_id": 458
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 41,
                            "slot_name": "华润海湾中心",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "华润海湾中心项目位于东海岸新城新津片区，总占地面积120亩，总建筑面积35.85万平方米，总投资约25亿元，包含东海岸新城首个大型购物中心万象天地及高品质住宅。项目将于2023年12月竣工验收并投入使用。",
                                "text_id": 459
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 42,
                            "slot_name": "汕头大学·香港中文大学联合汕头国际眼科中心易地扩建项目",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头大学·香港中文大学联合汕头国际眼科中心易地扩建项目位于东海岸新城新津片区，总占地面积20亩，总建筑面积5.7万平方米，总投资3.85亿元。项目规划床位300张，项目将于2022年12月竣工验收并投入使用。",
                                "text_id": 460
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 43,
                            "slot_name": "华侨试验区国家示范性高中和国际学校项目",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "华侨试验区国家示范性高中和国际学校项目位于东海岸新城新津片区，总占地面积135亩，总建筑面积15万平方米，总投资8.86亿元。项目将于2021年4月竣工验收并投入使用。",
                                "text_id": 461
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 44,
                            "slot_name": "汕头金中华侨试验区学校",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头金中华侨试验区学校位于东海岸新城新津片区，总占地面积66亩，总建筑面积2.8万平方米，总投资1.26亿元。现有在校生近1500人，36个教学班。",
                                "text_id": 462
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 45,
                            "slot_name": "汕头华侨试验区金湾学校",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头华侨试验区金湾学校位于东海岸新城新津片区，占地面积83.4亩，总建筑面积4.42万平方米，总投资约2.30亿元，是龙湖区政府批准设立的九年一贯制公办学校，已于2020年8月竣工并交付使用。",
                                "text_id": 463
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 46,
                            "slot_name": "津湾、东海岸公园",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "津湾、东海岸公园项目位于东海岸新城新津片区，总用地面积约625 亩，总投资约3.4亿元。其中：公园绿地397 亩，防护绿地115 亩，河涌水体75 亩，供电及社会停车场38 亩。项目将于2020年10月竣工验收并开园。",
                                "text_id": 464
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 47,
                            "slot_name": "侨韵文化旅游商业带",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头市侨韵文化旅游商业带项目位于汕头东海岸新城新溪、塔岗围片区北部主河涌两岸，总投资约13.7亿元，拟建设河涌绿地面积245.85公顷。项目将于2021年11月竣工验收并投入使用。",
                                "text_id": 465
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 48,
                            "slot_name": "汕头市东海岸新城地下综合管廊工程",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头市东海岸新城地下综合管廊工程位于东海岸新城新溪片区，总投资约18.97亿元。项目采用电力、通讯、给水、燃气管线入廊的方案，敷设干线管廊12.75 千米，过街管廊2.8 千米，是粤东地区首个城市地下综合管廊项目。项目将于2021年6月竣工验收并投入使用。",
                                "text_id": 466
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 49,
                            "slot_name": "汕头大学东校区暨亚青会场馆",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头大学东校区暨亚青会场馆项目位于东海岸新城塔岗围片区，规划总用地面积1551亩，总建筑面积约82万平方米，总投资约70亿元，分四期规划建设。一期为场馆区（“一场两馆”），二期为学生宿舍区（运动员村），一、二期计划于2021年5月底前建成；三期为教学实验区，计划于2022年6月底前建成；四期为扩容新增建设用地，计划于2024年底前建成。项目建成后可容纳2万名全日制在校生。",
                                "text_id": 467
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 50,
                            "slot_name": "汕头市中心医院易地重建项目（重大疫情救治基地）",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头市中心医院易地重建项目位于东海岸新城塔岗围片区，规划占地面积197.79亩，总建筑面积51.3万平方米，总投资约46亿元。项目设置床位3000张，建设内容包含设置国际医疗部，提供环境优越的高端医疗服务。遇重大疫情时，医院可快速转换为重症患者救治基地。项目将于2022年8月竣工验收并投入使用。",
                                "text_id": 468
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 51,
                            "slot_name": "龙湖中央商务区",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "龙湖中央商务区以高铁客运站汕头站为核心，规划面积约47平方公里，核心区面积约3.5平方公里，借助高铁枢纽客运站建设契机，整合广梅汕铁路增建二线、汕汕铁路（350高铁）、地铁、城际和轻轨等轨道交通资源，通过推动综合交通枢纽的建设带动周边片区的发展，形成城中有站，站中有城的汕头新门户和综合性城市中心。",
                                "text_id": 469
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 52,
                            "slot_name": "汕头高铁站综合交通枢纽",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头高铁站综合交通枢纽总规模11台23线，包括高铁普铁8台17线，城际铁路3台6线；计划建设10万平米的现代化高铁站房和占地6.3万平米的站前广场；预计2023年建成。汕头站将建设成为集高铁、普铁、城际铁路、城市轨道、公路客运、城市公交等多种方式于一体，便捷换乘的高质量综合交通枢纽，并以此为核心，站城融合，打造一流的中央商务区。",
                                "text_id": 470
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 53,
                            "slot_name": "新津片区",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "规划面积5.18平方公里，重点发展科技金融、休闲娱乐和高端居住产业",
                                "text_id": 471
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 54,
                            "slot_name": "新溪片区",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "规划面积11.7平方公里，重点发展数字经济、贸易会展、文化创意产业",
                                "text_id": 472
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 55,
                            "slot_name": "塔岗围片区",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "规划面积7.4平方公里，重点发展休闲旅游、科教文卫产业",
                                "text_id": 473
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 56,
                            "slot_name": "珠港新城",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "珠港新城是华侨试验区核心区和直管区的重要组成部分，规划面积3.51平方公里。重点打造粤东区域性总部乃至世界侨商潮商总部经济区，以文化传承、低碳交通、生态绿城为理念，构筑新城空间结构，高标准打造汕头总部经济区",
                                "text_id": 474
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 57,
                            "slot_name": "东海岸新城",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "东海岸新城是华侨试验区核心区和直管区的重要组成部分，规划面积24平方公里，其中陆域约20平方公里，包括津湾、溪湾、莱湾三个片区。规划定位为粤东区域综合服务中心、城市中央商务区、行政文化中心和生态型海岸新城",
                                "text_id": 475
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 58,
                            "slot_name": "华侨试验区人才大厦",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "汕头华侨试验区人才大厦共7层，面积5800平方米，配套党群服务中心、人才服务中心、创客办公室、68套人才公寓、多功能厅、健身房等功能区，是中共汕头市委组织部牵头华侨试验区共同打造的华侨华人、潮籍英才回国回乡创新创业“归谷”和各类人才拎包入驻的综合服务平台，加挂广东省“扬帆计划”汕头市人才驿站分站牌子。",
                                "text_id": 476
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 59,
                            "slot_name": "路网",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "珠港新城规划范围内包括5条城市主干道，分别为泰山路南延段、中山东路、海滨路东延段、天山南路、嵩山南路等；以及4条次干道，分别为珠城路、衡山路、黄山路、海兴路。东海岸新城内部三个片区通过全长16公里的“一路两桥”即东海岸大道和新津大桥、东海岸大桥连接贯通；同时三个片区分别通过13条南北向的主次干道与北侧腹地连接，形成密集的对外交通网络布局。未来东海岸新城将依托中阳大道快速路强化片区的道路网络体系。",
                                "text_id": 545
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 60,
                            "slot_name": "试验区规划建设情况",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "华侨试验区规划面积480平方公里，其中直管区规划面积28.82平方公里，包括珠港新城、东海岸新城和蓝水星片区。珠港新城3.51平方公里，产业方向以总部经济为主；东海岸新城新津片区（含蓝水星片区）6.23平方公里，产业方向以科技金融、休闲娱乐、高端商住为主；东海岸新城新溪片区11.7平方公里，产业方向以科技信息、贸易会展、文化创意为主；东海岸新城塔岗围片区7.4平方公里，产业方向以休闲旅游、科教文卫为主。目前，直管区范围内在建、已建市政道路总长约60公里，东海岸新城25公里海堤已完成，正全面推进公园绿地、综合管廊、学校、医院等基础设施和公共配套设施建设。",
                                "text_id": 478
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 61,
                            "slot_name": "试验区产业发展情况",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "根据国务院的批复要求和试验区产业发展定位，试验区重点发展跨境金融、商务会展、资源能源交易、文化创意、旅游休闲、教育培训、医疗服务、信息、海洋等九大都市产业。目前，试验区正着力发展金融服务业、总部经济等现代服务业和数字经济、人工智能、供应链等新产业新业态。整个直管区现有产业项目13个，总投资量约290亿元；存量登记注册企业691家，总注册资本456.87亿元",
                                "text_id": 541
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 62,
                            "slot_name": "亚青会全称",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会的全称是亚洲青年运动会，简称亚青会，是亚洲规模最大的青年综合性运动会，由亚洲奥林匹克理事会的成员国轮流主办。国际奥林匹克委员会承认亚洲青年运动会为正式的亚洲地区青年运动会。",
                                "text_id": 480
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 63,
                            "slot_name": "亚青会多久举办一次",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会每四年举办一届，自2009年开始第1届，2017年举办了第2届，会在2021年举办第三届，举办地在中国汕头",
                                "text_id": 481
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 64,
                            "slot_name": "第几届亚青会",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "本次汕头2021年举办的是第三届亚青会",
                                "text_id": 528
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 65,
                            "slot_name": "亚青会举办时间",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会将于2021年11月20日-2021年11月28日在中国汕头举行",
                                "text_id": 523
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 66,
                            "slot_name": "亚青参赛地区数",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会的参赛国主要分布在东亚，东南亚，南亚，西亚，中亚，包含45个国家及地区",
                                "text_id": 529
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 67,
                            "slot_name": "亚青会会徽",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会最新版会徽于2006年12月2日在多哈亚运会期间公布，中央是红日，红日上面盘环绕着一条龙，下面环绕着一只鹰，代表亚洲的团结，并强调了东方巨龙中国以及鹰所代表的阿拉伯国家在亚洲体育中所起的重要作用。会徽下方是五环以及“Olympic Council of Asia”的字样",
                                "text_id": 524
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 68,
                            "slot_name": "亚青会项目数",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会一共有18个大项：田径；水上运动包含游泳、跳水、水球；羽毛球；3*3篮球；沙滩排球；龙舟；足球；体操；高尔夫；手球；街舞；攀岩；橄榄球；冲浪；乒乓球；跆拳道；帆板和武术",
                                "text_id": 530
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 69,
                            "slot_name": "亚青会组织建设进度",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "亚青会组织建设，是自2019年3月3日亚青会申办成功以来，汕头充分调动全市力量投入到这项工作当中。5月18日成立筹备工作领导小组，下设办公室，由分管市领导具体抓日常工作，2020年成立执委会，已开始分期分批从全市选调人员，全脱产参加执委会工作，执委会下设办公室、竞赛部、场馆建设部、文化交流部、外联部等16个部门。",
                                "text_id": 527
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 70,
                            "slot_name": "场馆建设情况",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "本次汕头亚青会会场馆建设是按照“节俭办赛”原则，汕头充分利用现有场馆设施，在建设阶段就充分考虑场馆的赛后利用。场馆建设主要分两部分： 第一，新建两个场馆。一个是作为举办开幕式和田径、体操比赛的亚青会主场馆，另一个是承担大量比赛项目的体育运动产业基地，是结合新体校建设，在原来的游泳跳水馆基础上进行扩建。 第二，改造升级20个现有场馆，目前大部分项目已完成立项，开始维修改造，今年底前完成改造11个，剩余9个项目最迟于明年3月投入使用。这部分场馆赛后将作为学校教学、重要文体活动场所和全民运动健身、省级体育赛事等活动场所。",
                                "text_id": 525
                            },
                            "is_add_round": False
                        },
                        {
                            "slot_id": 71,
                            "slot_name": "亚青会的整体统筹和竞赛组织情况",
                            "use_custom_reply": True,
                            "custom_reply": {
                                "text": "本次汕头亚青会按照举办时间2021年，倒排工作周期，聘请国家级专家顾问，制定总体策划方案，明晰时间表、路线图，按照规划、准备、运行、总结四个阶段，梳理出92项重要任务节点。 推进信息化建设，着力打造“智慧亚青”。开展亚青会信息技术与通信系统规划编制，目前已完成规划初稿。推动场馆建设与信息化建设同步实施，充分运用5G、人工智能、4K/8K等新一代信息技术，提升场馆信息化水平。",
                                "text_id": 526
                            },
                            "is_add_round": False
                        }
                    ],
                    "label_id": None,
                    "child_node_jump_list": [
                        {
                            "condition_type": "slot",
                            "condition_value": {
                                "id": 72,
                                "name": "要求结束"
                            },
                            "child_condition": {
                                "id": 72,
                                "name": "要求结束"
                            },
                            "jump_to": {
                                "id": 402,
                                "name": "静默结束",
                                "node_type_name": "end",
                                "play_id": 18
                            }
                        }
                    ],
                    "unrecognized_reply": [
                        {
                            "text_id": 195,
                            "text": "很抱歉，闻程没有听清楚，您可以再说一次吗？"
                        },
                        {
                            "text_id": 444,
                            "text": "闻程刚才开小差啦，您可以再说一次吗？"
                        }
                    ],
                    "node_name": "互动",
                    "max_round_reply": {
                        "text_id": 518,
                        "text": "您说的问题闻程还在学习中，让闻程为您介绍一下，华侨经济合作实验区重点规划之一的珠港新城项目情况吧。珠港新城是华侨试验区核心区和直管区的重要组成部分，规划面积3.51平方公里。重点打造粤东区域性总部乃至世界侨商、潮商总部经济区，以文化传承、交通低碳、生态绿城为理念，构筑新城空间结构，高标准打造汕头总部经济区"
                    },
                    "max_stay_round": 3,
                    "node_id": 348,
                    "label_value_id": None,
                    "label_value": None,
                    "node_type": "clarify",
                    "label": None,
                    "use_faq": False,
                    "faq_depository_ids": [],
                    "faq_max_round": 0,
                    "faq_exit_node_id": None,
                    "unrecognized_node_id": None,
                    "silent_node_id": None
                },
                {
                    "node_reply": {
                        "text_id": 519,
                        "text": "。"
                    },
                    "internal_intent_list": [],
                    "internal_slot_list": [],
                    "label_id": None,
                    "child_node_jump_list": [],
                    "unrecognized_reply": [
                        {
                            "text_id": None,
                            "text": None
                        }
                    ],
                    "node_name": "静默结束",
                    "max_round_reply": {
                        "text_id": None,
                        "text": None
                    },
                    "max_stay_round": 0,
                    "node_id": 402,
                    "label_value_id": None,
                    "label_value": None,
                    "node_type": "end",
                    "label": None,
                    "use_faq": False,
                    "faq_depository_ids": [],
                    "faq_max_round": 0,
                    "faq_exit_node_id": None,
                    "unrecognized_node_id": None,
                    "silent_node_id": None
                }
            ],
            "play_name": "展厅-总体规划展区（意图）",
            "play_id": 18,
            "play_description": "1",
            "placeholders": [
                [
                    "#person_name#",
                    "用户姓名"
                ],
                [
                    "#gender#",
                    "用户性别"
                ],
                [
                    "#birth_date#",
                    "出生日期"
                ],
                [
                    "#id_card#",
                    "身份证后四位"
                ],
                [
                    "#bank_card#",
                    "银行卡后四位"
                ],
                [
                    "#loan_amount#",
                    "贷款金额"
                ],
                [
                    "#loan_usage#",
                    "贷款用途"
                ]
            ],
            "information": {
                "repayment_channel": "",
                "organization_name": ""
            },
            "advanced_configs": {}
        },
        "utime": "2020-09-03-10-47-37"
    }
    data.append(info18)
    for info in data:
        # results存放取出数据，可去掉（text为要迭代搜索的key）
        pick_text(info, 'text', results=[])

    # 写入excel
    write_excel()