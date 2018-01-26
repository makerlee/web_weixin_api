#!/usr/bin/env python
# coding: utf-8
import pymysql


"""
jiyang.li create at 2018-01-25
保存历史聊天记录:
    文字类型的聊天记录保存到mysql
    图片视频的聊天记录保存到硬盘(后期会保存到文件服务器)

"""


class MysqlDao(object):
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = 'root'
        self.db = 'vdr'
        self.port = '3306'
        self.conn = None

    def openConn(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset="utf8")

    def closeConn(self):
        self.conn.close()


dao = MysqlDao()
dao.openConn()
dao.closeConn()

