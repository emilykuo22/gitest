# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:53:44 2020

@author: ASUS
"""
#---------------------------SQLite
import sqlite3

# 連接資料庫
# 路徑前須加"r" 避免"\"出現錯誤
conn = sqlite3.connect ("firstDB.db")

# 執行SQL指令SELECT
query = conn.execute("SELECT * FROM students")

# 印出資料查詢結果資料
for row in query:
    print(row[1],row[2],row[3])

conn.close()

#--------------------------新增資料

import sqlite3
record="Kenny,5678,ken@ifme,8888-8888"
content= record.split(",")

conn = sqlite3.connect ("firstDB.db") #連接資料庫
sql="INSERT INTO csvsample (id,password,email,phone) VALUES ('{0}','{1}','{2}','{3}')"
sql=sql.format(content[0],content[1],content[2],content[3])
print(sql)
new = conn.execute(sql) #執行SQL命令
print(new.rowcount)
conn.commit() #確認交易
conn.close() #資料庫關閉

#---------------------------新增資料表
import sqlite3

conn = sqlite3.connect ("firstDB.db")
sql="CREATE TABLE product (id TEXT,name TEXT,price TEXT)"

new = conn.execute(sql)

sqlrowdata="INSERT INTO product VALUES \
('001', 'pinktshirt','290'),\
('002', 'bluepant','590')"

newdata = conn.execute(sqlrowdata)
print(newdata.rowcount)

conn.commit()
conn.close()


#---------------------------MySQL
import pymysql

# 建立資料庫連結
db= pymysql.connect("localhost","root","1234","sqlearning",charset="utf8")
cursor=db.cursor() # 建立cursor物件

cursor.execute("SELECT * from students")
data= cursor.fetchall() #取出所有資料

for row in data:
    print(row[0],row[1],row[2])

db.close()
#---------------------------新增資料
import pymysql
db= pymysql.connect("localhost","root","1234","sqlearning",charset="utf8")
cursor=db.cursor() # 建立cursor物件

cursor.execute("SELECT * from students")

record="NULL,蔡依林,F,1982-10-12,jolin@gmail.com,0900-909-090,台北市民水路90號,157,40"
f=record.split(",")

sql="""INSERT INTO students (cID, cName, cSex,cBirthday,cEmail,cPhone,cAddr,cHeight,cWeight)
VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')"""

sql=sql.format(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8])
print(sql)

try:
    cursor.execute(sql)
    db.commit()
    print("新增一筆資料")
except:
    db.rollback()
    print("新增失敗")  

db.close()


sql="""INSERT INTO students VALUES 
('NULL','蔡依林','F','1982-10-12','jolin@gmail.com','0900-909-090',
'台北市民水路90號','157','40')"""

db.close()


#---------------------------函數運用
import pymysql
db= pymysql.connect("localhost","root","1234","sqlearning",charset="utf8")
cursor=db.cursor() # 建立cursor物件

cursor.execute("SELECT * FROM students")

sql="SELECT COUNT(DISTINCT cWeight) FROM students"
n=cursor.execute(sql)
n=cursor.fetchone()
print(n[0])


#---------------------------函數運用
import pymysql
db= pymysql.connect("localhost","root","1234","sqlearning",charset="utf8")
cursor=db.cursor() # 建立cursor物件

sql="SELECT AVG(cHeight) FROM students"
cursor.execute(sql)
n=cursor.fetchone()
print(n[0])


db.commit()
db.close()







