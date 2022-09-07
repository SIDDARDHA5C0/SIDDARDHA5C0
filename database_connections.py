# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:30:24 2022

@author: Siddardha
"""
import pandas as pd
#data=pd.read_excel("C:\\Users\\Siddardha\\OneDrive\\Documents\\Authentication_people_data_set.xlsx",sheet_name=0)
#print(data)
df1=pd.read_csv("C:\\Users\\Siddardha\\Downloads\\flavors_of_cocoa.csv",sep=",")

#print(df1.info())
print((df1["company"]=="Guatemala").max())
#print(df1)


