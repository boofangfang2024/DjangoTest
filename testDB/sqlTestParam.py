# -*- coding: UTF-8 -*-
import pymysql.cursors

def readSQL():
    name = input("Please input your name:")
    age = eval(input("Please input your age:"))
# sql参数化可以防止sql注入的问题
    insertSql = '''insert into student(name,age) values (%s,%s)'''
# 打开数据库连接
    coon = pymysql.connect(user='root', password='jwy@2017', db='school', port=3306, host='127.0.0.1', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# 获取数据库操作游标，即创建一个sql语句对象
    cursor = coon.cursor()
#执行sql语句
    bb = cursor.execute(insertSql, [name, age])

# 提交
#利用commit提交执行，为什么这个地方使用commit呢？因为连接数据库看作是一个事务，事务就要有开始，提交，和关闭三个动作形成一个完整的事务
    coon.commit()
# 关闭游标
    cursor.close()
# 关闭连接
    coon.close()

if __name__ == '__main__':
    readSQL()
    print('Done')
