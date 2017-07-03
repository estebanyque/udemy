#!/usr/bin/python

temperatures=[10,-20,-289,100]

def cel2far(c):
    f = c * 9 / 5 + 32
    return float(f)

with open("temperatures2.txt", 'a+') as file:
    for t in temperatures:
        if t > -273.15:
            file.write(str(cel2far(t))+"\n")
