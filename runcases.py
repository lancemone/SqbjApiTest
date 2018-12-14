#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 3:41 PM
# @Author  : Motao
# @Site    : 
# @File    : runcases.py
# @Software: PyCharm
import os
import pytest
from common.path_conf import PathConf as pathconf


class RunCases:
    def __init__(self):
        self.xml_report_path = pathconf().xml_report_path()
        self.allure_report_path = pathconf().allure_report_path()
        self.html_report_path = pathconf().html_report_path()
        self.casedir = os.path.join(os.getcwd(), "test_cases")
        print(self.casedir)
        print(self.allure_report_path)
        print(self.html_report_path)

    def run_cases(self):
        pytest.main(['-s', '-q', '%s' % self.casedir, '--alluredir', '%s' % self.xml_report_path])
        pytest.main(['-s', '-q', '%s' % self.casedir, '--html', '%s' % self.html_report_path])
        os.system('allure generate %s -o %s' % (self.xml_report_path, self.allure_report_path))


if __name__ == "__main__":
    a = RunCases()
    a.run_cases()
