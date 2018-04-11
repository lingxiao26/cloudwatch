#!/usr/bin/env python
# coding: utf-8
#
# db models

import MySQLdb as mysql
from conf import config


class CloudDb(object):
    def __init__(self):
        self.host = config.HOST
        self.user = config.USER
        self.passwd = config.PASSWD
        self.db = config.DB

    def connect(self):
        conn = mysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        cur = conn.cursor()
        return conn, cur

    def sql_commit(self, sql, args=()):
        conn, cur = self.connect()
        try:
            cnt = cur.execute(sql, args)
        except UnicodeEncodeError, e:
            print e
        conn.commit()
        cur.close()
        conn.close()
        # return cnt

    def sql_fetch(self, sql, args=()):
        rt_list = []
        conn, cur = self.connect()
        cur.execute(sql, args)
        rt_list = cur.fetchall()
        cur.close()
        conn.close()
        return rt_list


# if __name__ == '__main__':
#     db = CloudDb()
#     sql = 'insert into navigation (name, url) values (%s, %s)'
#     args = ('xiao', 'www.hello.com')
#     print db.sql_commit(sql, args=args)