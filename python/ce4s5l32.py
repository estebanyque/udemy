#!/usr/bin/python

temperatures=[10,-20,-289,100]

def cel2far(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9 / 5 + 32
        return float(f)

for t in temperatures:
    print(cel2far(t))
