#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 7:06 PM
# @Author  : Motao
# @Site    : 
# @File    : config.py
# @Software: PyCharm

import codecs
import os
import configparser


prodir = os.path.split(os.path.realpath(__file__))[0]
confpath = os.path.join(prodir, "config.ini")


class ReadConf:
    # titles
    TITLE_EMAIL = "EMAIL"
    TITLE_DATABASE = "DATABASE"
    TITLE_PARAMS = "PARAMS"
    TITLE_HTTP = "HTTP"
    TITLE_HEADER = "HEADER"

    def __init__(self):
        if not os.path.exists(confpath):
            raise FileExistsError("配置文件不存在!")
        else:
            fb = open(confpath)
            conf = fb.read()
            # remove BOM
            if conf[:3] == codecs.BOM_UTF8:
                conf = conf[3:]
                file = codecs.open(confpath, "w")
                file.write(conf)
                file.close()
            fb.close()
            self.cf = configparser.ConfigParser()
            self.cf.read(confpath)

    def get_email(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get(ReadConf.TITLE_EMAIL, name)
        return value

    def get_db(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get(ReadConf.TITLE_DATABASE, name)
        return value

    def get_http(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get(ReadConf.TITLE_HTTP, name)
        return value

    def get_params(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get(ReadConf.TITLE_PARAMS, name)
        return value

    def get_header(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get(ReadConf.TITLE_HEADER, name)
        return value

    def set_header(self, name, value):
        '''

        :param name:
        :param value:
        :return:
        '''
        self.cf.set(ReadConf.TITLE_HEADER, name, value)
        with open(confpath, "w+") as f:
            self.cf.write(f)

    def set_value(self, v_title, name, value):
        '''

        :param v_title:
        :param name:
        :param value:
        :return:
        '''
        self.cf.set("%s" % v_title, name, value)
        with open(confpath, "w+") as f:
            self.cf.write(f)

