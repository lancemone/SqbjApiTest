#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 7:32 PM
# @Author  : Motao
# @Site    : 
# @File    : path_conf.py
# @Software: PyCharm
import os
import shutil


class PathConf:
    def report_path(self):
        rep_path = os.path.split(os.path.abspath(__file__))[0]
        report_path = os.path.join(os.path.split(rep_path)[0], "report")
        # print(report_path)
        if os.path.exists(report_path):
            return report_path
        else:
            os.mkdir(report_path)
            return report_path

    def xml_report_path(self):
        report_path = self.report_path()
        xml_report_path = os.path.join(report_path, "xml")
        if os.path.exists(xml_report_path):
            if os.listdir(xml_report_path) is []:
                return xml_report_path
            else:
                shutil.rmtree(xml_report_path)  # 递归删除文件夹
                os.mkdir(xml_report_path)
                return xml_report_path
        else:
            os.mkdir(xml_report_path)
            return xml_report_path

    def allure_report_path(self):
        report_path = self.report_path()
        allure_report_path = os.path.join(report_path, "allure_html")
        if os.path.exists(allure_report_path):
            if os.listdir(allure_report_path) is []:
                return allure_report_path
            else:
                shutil.rmtree(allure_report_path)  # 递归删除文件夹
                os.mkdir(allure_report_path)
                return allure_report_path
        else:
            os.mkdir(allure_report_path)
            return allure_report_path

    def html_report_path(self):
        report_path = self.report_path()
        html_path = os.path.join(report_path, "html")
        html_report_path = os.path.join(html_path, "html_report.html")
        if os.path.exists(html_path):
            if os.listdir(html_path) is []:
                open(html_report_path, 'w').close()
                return html_report_path
            else:
                shutil.rmtree(html_path)  # 递归删除文件夹
                os.mkdir(html_path)
                open(html_report_path, 'w').close()
                return html_report_path
        else:
            os.mkdir(html_path)
            open(html_report_path, 'w').close()
            return html_report_path

    def jenkins_allure_path(self):
        rep_path = os.path.split(os.path.abspath(__file__))[0]
        report_path = os.path.join(os.path.split(rep_path)[0], "allure-results")
        # print(report_path)
        if os.path.exists(report_path):
            return report_path
        else:
            os.mkdir(report_path)
            return report_path

