# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BMP_03
# FileName:      test
# Author:        ZJY
# Datetime:      2022/6/6 15:40
# Description：
# -----------------------------------------------------------------------------------
# import allure
# import pytest
#
#
# def test_01():
#     print(11)
#     global id
#     id = 123
#     assert 1 == 1
#
#
# def test_02():
#     print(id)
#     assert 2 == 2
#
#
# if __name__ == '__main__':
#     pytest.main()



dict1 = {'code': 'test43addorg', 'demId': '1', 'exceedLimitNum': 0, 'grade': '', 'limitNum': 0, 'name': 'test43addorg', 'nowNum': 0, 'orderNo': 0, 'parentId': '0'}
print(dict1['demId'])
if 'demId' in dict1.keys():
    print(dict1['demId'])