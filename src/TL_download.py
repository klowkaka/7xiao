#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
def getcode():
    # 打开数据库连接
    db = MySQLdb.connect("localhost","root","root","test" )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    codelist=[]
    idx=0
    # SQL 查询语句
    sql = "select distinct code  from report_data_2016_3 order by code;"
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       for row in results:
            code = row[0]
            codelist.append(code)
            # 打印结果
            
    except:
       print "Error: unable to fecth data"
    #print codelist
    # 关闭数据库连接
    db.close()
    return codelist
