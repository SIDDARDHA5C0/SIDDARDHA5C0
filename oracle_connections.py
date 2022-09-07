# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 12:47:31 2022

@author: Siddardha
"""
"""
import oracledb
#import db_config
con = oracledb.connect('student/student@localhost:1521/student')
#con = oracledb.connect(user="student", password="stuent")
print("Database version:", con.version)"""
"""import oracledb

print("Default array size:", oracledb.defaults.arraysize)"""
"""
import cx_Oracle

#userpwd = ". . ." # Obtain password string from a user prompt or environment variable

connection = cx_Oracle.connect(user="student", password="student",
                               dsn="dbhost.example.com/orcl/dater",
                               encoding="UTF-8")"""
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'student', password='student', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute('select * from database.table')
