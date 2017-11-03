# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:34:18 2017

@author: limbub
"""
import pandas as pd

filename = 'employee_data.csv'
data = pd.read_csv(filename,header=None)#saves the files as a dataframe
print(data)

print(data.index)
print(data.index.name)
print(data.columns.values)
data.columns = ['Name','Role','cost','Salary']
#data['Role'].str.strip()
data['Role']=data['Role'].map(lambda x:x.strip(' '))
print(data.columns.values)
data.set_index('Role',inplace=True)
print(data)
print(data.columns.values)
print(data.index)
print(data['Salary'].loc['Marketing'].mean(axis=0))
#print(g3)
