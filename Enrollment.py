# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:46:01 2022

@author: Siddardha
"""
from datetime import date
import mysql.connector 
conn=mysql.connector.connect(host="localhost",password="Database@system1",user="root", database="db")
if conn.is_connected():
    print("hai");
mycursor = conn.cursor()
a="hai12"
b="hello1111"
c= date.today()



sql = "INSERT INTO db.attendence (name,rollno,date) VALUES (%s, %s,%s)"
val = (a,b,c)
mycursor.execute(sql, val)
conn.commit()

print("1 record inserted, ID:", mycursor.lastrowid)


mycursor.execute("SELECT * FROM db.attendence")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



#d="insert into db.attendence(name,rollno,date) values('{0}','{1}','{2}')".format(a,b,c)
#print(d)
#e="select  * from db.attendence"
#mycursor.execute(d)
#f=mycursor.execute("select * from db.attendence") 

