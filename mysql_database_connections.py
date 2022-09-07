# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 20:52:40 2022

@author: Siddardha
"""

import mysql.connector 
conn=mysql.connector.connect(host="localhost",password="Database@system1",user="root", database="db")
if conn.is_connected():
    print("hai");
mycursor = conn.cursor()

mycursor.execute("CREATE TABLE attendence (name VARCHAR(255), rollno VARCHAR(255))")
    