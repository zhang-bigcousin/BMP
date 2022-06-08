# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BMP_request
# FileName:      test_pytest
# Author:        ZJY
# Datetime:      2022/6/4 11:16
# Description：
# -----------------------------------------------------------------------------------
import allure
import pytest

from tool.read_excel import ReadExcel


class TestBmp:
    @allure.epic("BPM系统")
    @pytest.fixture(scope='session')
    def read_excel(self):
        read_excel = ReadExcel('path', 'excel_path', 'Sheet1')
        yield read_excel

    @pytest.mark.parametrize('module, interface, title, request_method, url, params_types, data_case, expect_data, '
                             'row, sql_types, sql, new_key',
                             ReadExcel('path', 'excel_path', 'Sheet1').get_case_data_list())
    def test_01(self, request_bmp, connect_db, read_excel, open_case_data, open_data_sql,
                module, interface, title, request_method, url, params_types, data_case,
                expect_data, row, sql_types, sql, new_key):

        # 用于allure报告里面分级
        allure.dynamic.feature(module)
        allure.dynamic.story(interface)
        allure.dynamic.title(title)
        # allure.dynamic.severity(level)

        # 利用套件对数据进行拆分和sql语句运行和数据更新
        new_data = open_data_sql(sql_types, sql, new_key, params_types, data_case)
        params_data = new_data[0]
        json_data = new_data[1]
        # print(params_data, json_data)

        # 执行请求
        result = request_bmp.all_request(request_method, url, params_types, params_data, json_data)

        # 断言
        try:
            for key in expect_data.keys():  # expect_data字典类型
                assert result.json()[key] == expect_data[key]  # 预期结果放在后面
                # assert case_expect[key] == result.json()[key]
        except:
            read_excel.save_result('失败', row)
            # print(case_expect,result.json())
            raise AssertionError('断言失败')
        else:
            read_excel.save_result('成功', row)
        finally:
            print(row, result.json(), expect_data, result.url)


if __name__ == '__main__':
    pytest.main()
