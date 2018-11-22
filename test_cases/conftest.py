#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 6:16 PM
# @Author  : Motao
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
import time
import logging
import pytest
from common.log_conf import logger


@pytest.fixture(scope="module", autouse=True)
def mod_log(request):
    logging.captureWarnings(True)
    logger.info('-----------------')
    logger.info('module      : %s test start' % request.module.__name__)
    logger.info('-----------------')
    yield mod_log
    logger.info('-----------------')
    logger.info('module      : %s test finished' % request.module.__name__)
    logger.info('-----------------')


@pytest.fixture(autouse=True)
def fun_log(request):
    logger.info('-----------------')
    logger.info('function    : %s test start' % request.function.__name__)
    logger.info('time        : %s' % time.asctime())
    logger.info('-----------------')
    yield mod_log
    logger.info('-----------------')
    logger.info('function    : %s test finished' % request.function.__name__)
    logger.info('-----------------')


