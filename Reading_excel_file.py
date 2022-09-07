# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:49:11 2022

@author: Siddardha
"""
import pandas as pd
#data=pd.read_excel("C:\\Users\\Siddardha\\OneDrive\\Documents\\Authentication_people_data_set.xlsx",sheet_name=0)
#print(data)
df1=pd.read_excel("C:\\Users\\Siddardha\\OneDrive\\Documents\\Authentication_people_data_set.xlsx", sheet_name=0)

#print(df1)
#print(df1.info())
#print(df1.head())
print(df1.columns)
#print(df1["RNO"])
df1[['RNO',"NAME OF STUDENT"]] = df1[['RNO',"NAME OF STUDENT"]].astype('string')
print(df1["RNO"]+" "+df1["NAME OF STUDENT"])
print(type(df1["NAME OF STUDENT"]))

print(list(df1["RNO"]))
print(list(df1["NAME OF STUDENT"]))
#print(list(df2[""]))