#!/usr/bin/python

import datetime
import time

#now = datetime.datetime.now()
#yesterday = datetime.datetime(2016, 6, 6, 0, 0, 0)
#print(type(now))
#print(now)
#print(yesterday)

#delta = now - yesterday

#print(delta)
#print(delta.total_seconds())

filename = datetime.datetime.now()

def create_file():
    """This function creates a file"""
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt", 'w') as file:
        file.write("")

create_file()

lst = []

for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1)

print(lst)