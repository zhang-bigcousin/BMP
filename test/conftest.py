# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BMP_request
# FileName:      conftest
# Author:        ZJY
# Datetime:      2022/6/4 11:16
# Description：
# -----------------------------------------------------------------------------------
import pytest

from tool import connect_sql
from tool.connect_sql import ConnectDb
from tool.read_excel import ReadExcel
from tool.request_bmp import RequestBmp


@pytest.fixture(scope="session")
# 获取请求
def request_bmp():
    resp = RequestBmp()
    yield resp


@pytest.fixture(scope='session')
# 数据库操作
def connect_db():
    conn_db = ConnectDb()
    yield conn_db
    conn_db.db_close()


dict1 = {}


@pytest.fixture(scope='session')
def demo1(key, value):
    def _set_value(key, value):
        dict1[key] = value

    yield _set_value


@pytest.fixture(scope='session')
def demo2():
    def _get_value(key):
        return dict1[key]

    yield _get_value


# 拆分数据
@pytest.fixture(scope='session')
def open_case_data():
    def open_data(params_types, data_case):
        json_data, params_data = None, None
        if params_types:
            # json_data, params_data = None, None
            for i in range(len(params_types)):
                # 转换为小写方便判断
                params_type = params_types[i].lower()
                if params_type == 'query':
                    params_data = data_case[i]
                    # return self.session.get(url, params=data_case)
                elif params_type == 'body':
                    json_data = data_case[i]
                    # return self.session.get(url, json=data_case)
        return params_data, json_data

    yield open_data


# sql语言分类
# for循环读取列表
@pytest.fixture(scope='session')
def open_data_sql(connect_db, open_case_data):
    def open_sql(sql_types, sql, new_key, params_types, data_case):

        # 利用自定义固件函数拆分data_case,获取 json_data,params_data
        open_case_datas = open_case_data(params_types, data_case)
        params_data = open_case_datas[0]
        json_data = open_case_datas[1]

        num_key = 0  # 当多个需要更新的是值时候,用于取new_key中的对应select的元素
        if sql_types:
            for i in range(len(sql_types)):
                # 全部转换为小写方便后面判断,注意:lower()是字符串的方法
                sql_type = sql_types[i].lower()

                if sql_type == 'delete':
                    # 判断是否语句为空
                    if sql[i]:
                        del_sql = sql[i]
                        # 执行sql语句
                        connect_db.sql_delete(del_sql)

                # 判断sql语句类型
                elif sql_type == 'select':
                    # 判断是否语句为空
                    if sql[i]:
                        sel_sql = sql[i]
                        sql_result = connect_db.sql_select(sel_sql)
                        # 判断需要更新的key属于json_data还是params_data
                        # print(new_key,json_data)
                        # 判断params_data和json_data不为空
                        if params_data:
                            if new_key[num_key] in params_data:
                                params_data[new_key[num_key]] = sql_result
                        if json_data:
                            if new_key[num_key] in json_data:
                                json_data[new_key[num_key]] = sql_result
                        num_key += 1
        return params_data, json_data

    return open_sql



# 汉化测试的标题
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf_8').decode('unicode_escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode_escape')
