#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 11:47 AM
# @Author  : Motao
# @Site    : 
# @File    : send_email.py
# @Software: PyCharm

import smtplib
import time
import os
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common import log_conf
from config import config
from common import consts


class SendEmail:

    def __init__(self):
        self.logger = log_conf.logger
        self.conf = config.ReadConf
        self.smtp_server = self.conf.get_email(name="smtp_server")
        self.mail_user = self.conf.get_email(name="mail_user")
        self.mail_pass = self.conf.get_email(name="mail_pass")
        self.mail_port = self.conf.get_email(name="mail_port")
        self.receiver = self.conf.get_email(name="receiver")
        self.subject = self.conf.get_email(name="subject")
        self.testuser = self.conf.get_email(name="testuser")
        self.on_off = self.conf.get_email(name="on_off")
        self.stress = consts.STRESS_LIST
        self.result = consts.RESULT_LIST

    def sent_email(self, file_html):
        tm = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
        file = open(file_html, "r", encoding='UTF-8').read()
        subject = self.subject + tm
        body = 'Hi，all\n本次接口自动化测试报告如下：\n   接口响应时间集：%s\n   接口运行结果集：%s' % (self.stress, self.result)
        # text = MIMEText(sendfile, "base64", "utf-8")   第一个是邮件正文，第二个是设置文本格式，第三个则用于设置文本编码
        text = MIMEText(file, "html", "utf-8")
        # 邮件内容
        msgRoot = MIMEMultipart()
        msgRoot["Subject"] = Header(subject, 'utf-8')
        # msgRoot["From"] = _format_addr(sender)
        # msgRoot["To"] = _format_addr(receiver)
        msgRoot["From"] = self.mail_user
        msgRoot["To"] = ','.join(self.receiver)
        msgRoot.attach(body)
        msgRoot.attach(text)
        # 添加附件
        att = MIMEApplication(open(file_html, 'rb').read())
        att["Content-Type"] = "application/octet-stream"
        att.add_header("Content-Disposition", "attachment", filename='API自动化测试报告.html')
        # att["ContenT-Disposition"] = "attachment;filename = 'API自动化测试报告.html '"
        msgRoot.attach(att)

        try:
            smtp = smtplib.SMTP_SSL(self.smtp_server, self.mail_port)
            smtp.login(self.mail_user, self.mail_pass)
            smtp.sendmail(self.mail_user, self.receiver, msgRoot.as_string())
        except Exception as e:
            self.logger.error(e)
            self.logger.info('邮件发送失败，请检查邮件配置!')
        else:
            print("发送成功")
            self.logger.info("邮件发送成功")
        finally:
            smtp.quit()

    def find_html(self, html_path):
        lists = os.listdir(html_path)
        lists.sort(key=lambda fn: os.path.getmtime(html_path + "/" + fn))   # linux系统
        # lists.sort(key=lambda fn: os.path.getmtime(test_report+"\\"+fn))    # 按时间排序win
        file_html = os.path.join(html_path, lists[-1])
        self.logger.info("测试报告文件" + file_html)
        return file_html













