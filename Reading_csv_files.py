# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 09:25:43 2022

@author: Siddardha
"""

import pandas as pd
#df=pd.read_csv("C:\\Users\\Siddardha\\OneDrive\\Documents\\Data_file_of_people.csv",sep=",")
df1=pd.read_excel("C:\\Users\\Siddardha\\OneDrive\\Documents\\Data_file_of_people.xlsx", sheet_name=0)
#print(df1)

print(df1.info())
print(df1[1])
#a=df1["column1"].to_list()
a=list(df1[1][:])
print(a)
#df1[0].astype("string")

#print(df1.info())

#print(df)
"""df2=pd.read_excel("C:\\Users\\Siddardha\\OneDrive\\Documents\\Data_file_of_people.xlsx", sheet_name=1)
print(df2)"""