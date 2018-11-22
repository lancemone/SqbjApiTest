#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 3:41 PM
# @Author  : Motao
# @Site    : 
# @File    : runcases.py
# @Software: PyCharm
import os
import shutil
import pytest


class RunCases:
    def __init__(self):
        self.xml_report_path = self.xml_report_path()
        self.allure_report_path = self.allure_report_path()
        self.html_report_path = self.html_report_path()
        self.casedir = os.path.join(os.getcwd(), "test_cases")



    def run_cases(self):
        pytest.main(['-s', '-q', '%s' % self.casedir, '--alluredir', '%s' % self.xml_report_path])
        pytest.main(['-s', '-q', '%s' % self.casedir, '--html', '%s' % self.html_report_path])
        os.system('allure generate %s -o %s' % (self.xml_report_path, self.allure_report_path))


if __name__ == "__main__":
    a = RunCases()
    a.run_cases()
