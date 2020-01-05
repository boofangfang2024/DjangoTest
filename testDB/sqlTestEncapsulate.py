# -*- coding: UTF-8 -*-
import pymysql.cursors

class Helper(object):
    '''封装连接数据库，插入数据，查询数据的方法'''
    def __init__(self, host, port, db, user, password, charset="utf-8"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.port = port

    def open(self):
        '''打开数据库'''
        self.coon = pymysql.connect(host = self.host, port = self.port, db = self.db, user = self.user, password = self.password, charset = self.charset, cursorclass=pymysql.cursors.DictCursor)
        #创建游标对象
        self.cursor = self.coon.cursor()


    def cub(self, sql, params):
        '''插入数据'''
        try:
            self.open()
            #创建sql语句
            sql = "insert into student(name,age) values (%s,%s)"
            #执行sql语句
            self.cursor.execute(sql, params)
            #提交事务
            self.coon.commit()
        except Exception as e:
            print(e)

    def all(self,sql):
        '''查询数据'''
        try:
            self.open()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    def __del__(self):
        """关闭数据库"""
        # 魔术方法, 析构化 ,析构函数
        self.cursor.close()
        self.coon.close()

if __name__ == '__main__':
    h = Helper('127.0.0.1',3306,'school','root','c','utf8')
    h.open()
    result = h.all("select * from student")
    print(result)