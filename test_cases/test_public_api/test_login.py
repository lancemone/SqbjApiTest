#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 10:10 AM
# @Author  : Motao
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm
import allure
import pytest
from common import log_conf, consts
from allure import utils

logger = log_conf.logger


@allure.MASTER_HELPER.feature("test")
class TestLogin:
    def test_login(self, fun_log):
        assert 0 == 0
        logger.info("finish")
