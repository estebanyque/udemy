#!/usr/bin/python

import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]])

df1

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","Value"])

df1

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","Value"], index=["First","Second"])
