#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 10:38 AM
# @Author  : Motao
# @Site    : 
# @File    : test_get_tenant.py
# @Software: PyCharm

import requests
import pytest
import allure
import json
import os

@allure.feature("TestGetTenant")   # feature定义功能.标注主要功能模块
class TestGetTenant(object):

    @pytest.mark.parametrize("username, shortname", [
        (16811011101, "鑫泰产业"),
        (16811011101, "motest"),
        (16811011101, "jingj")

    ])
    @allure.story("验证获取用户租户接口")     # story定义用户场景
    @allure.feature('test_get_tenant')
    def test_get_tenant(self, username, shortname):
        '''

        用例描述：根据用户手机号验证此手机号返回的相应租户是否正确
        '''
        with allure.step("设置用户登录手机号"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中
            url = "https://smart.uat2.sqbj.com/api/basic/json-rpc/views"
            data = {"id": 1,
                    "jsonrpc": "2.0",
                    "method": "common_getTenantByUsername",
                    "params": [username]}
        with allure.step("获取用户租户信息"):
            r = requests.post(url=url, json=data, verify=False)
            r_code = r.status_code
            r_json = json.dumps(r.json())
            r_time = r.elapsed.microseconds/1000
            #res = r_json['result']
            print(r_json)
        with allure.step("验证结果"):
            assert r_code == 200
            assert shortname in r_json


if __name__ == "__main__":
    # os.system("py.test /Users/motao/PycharmProjects/SqbjApiTest/test_cases/ --alluredir /Users/motao/PycharmProjects/SqbjApiTest/TestReport/")
    pytest.main(['-s', '-q', 'test_get_tenant.py', '--alluredir', './report/'])
    # os.system('allure serve ./report/')













