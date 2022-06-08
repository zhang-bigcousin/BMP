# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BMP_request
# FileName:      connect_sql
# Author:        ZJY
# Datetime:      2022/6/3 23:37
# Description：
# -----------------------------------------------------------------------------------
import pymysql

from tool import read_ini


class ConnectDb:

    def __init__(self):
        # 创建数据库链接,游标
        # 读取ini数据
        ip = read_ini.ReadIni().get_after_path('mysql', 'ip')
        port = read_ini.ReadIni().get_after_path('mysql', 'port')
        database = read_ini.ReadIni().get_after_path('mysql', 'database')
        username = read_ini.ReadIni().get_after_path('mysql', 'user')
        password = read_ini.ReadIni().get_after_path('mysql', 'password')
        self.db = pymysql.Connection(
            host=ip,
            port=int(port),
            database=database,
            user=username,
            passwd=password
        )
        self.cursor = self.db.cursor()

    # 执行删除语句
    def sql_delete(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    # 执行查询语句(有返回值)
    def sql_select(self, sql):
        # 先查询
        self.cursor.execute(sql)
        # 在获取值
        result = self.cursor.fetchall()
        # fetchall没有值的时候返回(),有值返回的是二维元组
        if len(result) > 0:
            return result[0][0]

    def db_close(self):
        # 先关闭游标对象和再关闭链接对象
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    conn = ConnectDb()
    # str1 = "DELETE FROM uc_demension WHERE CODE_='test43gsdgffsd';"
    str2 = "SELECT ID_ FROM uc_demension WHERE IS_DELE_='0' LIMIT 1;"
    # conn.sql_delete(str1)
    print(conn.sql_select(str2))
