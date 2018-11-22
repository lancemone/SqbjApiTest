#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 7:53 PM
# @Author  : Motao
# @File    : log_conf.py
# @Software: PyCharm


import logging
import os
from datetime import datetime

report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "TestReport")
if not os.path.exists(report_path):
    os.mkdir(report_path)
pro_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = os.path.join(os.path.join(pro_dir, "TestReport"), "logout")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_file = os.path.join(log_dir, "%s.log" % (str(datetime.now().strftime("%Y%m%d%H%M%S"))))
logger = logging.getLogger("AutoTest")
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')  # 定义日志输出格式
ch = logging.StreamHandler()  # 日志输出到屏幕控制台
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
fh = logging.FileHandler(log_file)  # 日志输出到日志文件
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)

# logger.info(" start logging")
# logger.info(" start print log")

if __name__ == '__main__':
    logger.info(" start logging")
    logger.info(" start print log")

