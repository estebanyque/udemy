#!/usr/bin/python

import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]])

print(df1)

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","Value"])

print(df1)

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","Value"], index=["First","Second"])

df2=pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])

print(df2)

df2=pandas.DataFrame([{"Name":"John", "Surname":"Johns"},{"Name":"Jack"}]) 

print(type(df1))
