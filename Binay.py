# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:34:18 2017

@author: limbub
"""
import pandas as pd

filename = 'employee_data.csv'
data = pd.read_csv(filename,header=None)#saves the files as a dataframe
#print(data)                            #prints the data file
#print(data.index)                      #prints the values of the index
#print(data.index.name)                 #prints the name of the index if there is one
#print(data.columns.values)             #prints the values of the columns.
data.columns = ['Name','Role','Salary']
#data['Role'].str.strip()               #Tried this method. Doesn't seem to work
#data['Role']=data['Role'].map(lambda x:x.strip(' ')) #this is for stripping the spaces
#print(data.columns.values)              #prints the name of the columns.
#data.set_index('Role',inplace=True)     #Setting the 'Role' Column as the index
#print(data)                             
#print(data.columns.values)              #Prints the new column values
#print(data.index)                      #Prints the index
#print(data['Salary'].loc['Marketing'].mean(axis=0)) #Calculates the mean.
#print(g3)
df1 = data.groupby(['Role']).agg(['mean','count','max'])
df1.columns = ['avg','count','max_sal']
df2 = df1.sort_values('avg',ascending=False)
#print(df2)
#print(df1.index.name)
#print(df1.columns.values)
for index,row in df2.iterrows():
    if row['count'] >=8 and row['max_sal']<=152000:
        print(index, row['avg'])