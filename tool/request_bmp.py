# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BMP_request
# FileName:      request
# Author:        ZJY
# Datetime:      2022/6/3 23:37
# Description：
# -----------------------------------------------------------------------------------
import requests


class RequestBmp:

    def __init__(self):
        # 登录,获取token,session实例化
        resp = requests.post('http://140.246.124.176:8280/auth', json={'username': 'admin', 'password': 'MTIzNDU2'})
        token = resp.json()['token']
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/100.0.4896.127Safari/537.36", "Authorization": "Bearer " + token}
        self.session = requests.Session()
        self.session.headers.update(header)

    def all_request(self, request_method, url, params_types, params_data, json_data):
        # 将请求方法小写化,方便判断
        request_method = request_method.lower()
        # 判断
        if request_method == 'get':
            # 判断请求类型
            if params_types:
                # # json_data, params_data = None, None
                # for i in range(len(params_types)):
                #     # 转换为小写方便判断
                #     params_type = params_types[i].lower()
                #     if params_type == 'query':
                #         # params_data = data_case[i]
                #         # return self.session.get(url, params=data_case)
                #     elif params_type == 'body':
                #         # json_data = data_case[i]
                #         # return self.session.get(url, json=data_case)
                return self.session.get(url, json=json_data, params=params_data)
                # 请求类型可能为空的情况
            else:
                return self.session.get(url)

        elif request_method == 'post':
            # 判断请求类型
            # if params_types:
            #     json_data, params_data = None, None
            #     for i in range(len(params_types)):
            #         # 转换为小写方便判断
            #         params_type = params_types[i].lower()
            #         if params_type == 'query':
            #             params_data = data_case[i]
            #             # return self.session.get(url, params=data_case)
            #         elif params_type == 'body':
            #             json_data = data_case[i]
            #             # return self.session.get(url, json=data_case)
                return self.session.post(url, json=json_data, params=params_data)

        elif request_method == 'put':
            # 判断请求类型
            # if params_types:
            #     json_data, params_data = None, None
            #     for i in range(len(params_types)):
            #         # 转换为小写方便判断
            #         params_type = params_types[i].lower()
            #         if params_type == 'query':
            #             params_data = data_case[i]
            #             # return self.session.get(url, params=data_case)
            #         elif params_type == 'body':
            #             json_data = data_case[i]
            #             # return self.session.get(url, json=data_case)
                return self.session.put(url, json=json_data, params=params_data)

        elif request_method == 'delete':
            # # 判断请求类型
            # if params_types:
            #     json_data, params_data = None, None
            #     for i in range(len(params_types)):
            #         # 转换为小写方便判断
            #         params_type = params_types[i].lower()
            #         if params_type == 'query':
            #             params_data = data_case[i]
            #             # return self.session.get(url, params=data_case)
            #         elif params_type == 'body':
            #             json_data = data_case[i]
            #             # return self.session.get(url, json=data_case)
                return self.session.delete(url, json=json_data, params=params_data)

        else:
            print('只支持get、post、put、delete四种请求方式')


if __name__ == '__main__':
    request = RequestBmp()

    # ['POST',
    # 'C:\\Users\\Administrator\\Desktop\\python\\BMP_request\\http://140.246.124.176:8280/auth',
    # 'body', {'username': 'admin', 'password': 'MTIzNDU2'}
    print(request.all_request(request_method='POST', params_types=['body'],
                               data_case=[{'code': 'test43gsdgffsd', 'description': 'test43gsdgffsd', 'isDefault': 0, 'name': 'test43gsdgffsd'}],
                               url=r'http://140.246.124.176:8280/api/demension/v1/dem/addDem').json())
