# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BMP_request
# FileName:      read_ini
# Author:        ZJY
# Datetime:      2022/6/2 10:12
# Description：
# -----------------------------------------------------------------------------------
import configparser
import os


class ReadIni:

    def __init__(self):
        # 实例化对象
        self.config = configparser.ConfigParser()
        # 获取当前目录的父级目录
        self.before_path = os.path.dirname(os.path.dirname(__file__))
        # 读取ini文件
        self.config.read(self.before_path + r'/config/data_ini.ini')

    # 获取完整的路径
    def get_all_path(self, section, option):
        return self.before_path + self.config.get(section, option)

    # 仅仅获取文件里面的路径
    def get_after_path(self, section, option):
        return self.config.get(section, option)


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_after_path('host', 'bmp_host'))
    print(read_ini.get_all_path('path', 'excel_path'))

