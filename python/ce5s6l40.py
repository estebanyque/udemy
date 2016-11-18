#!/usr/bin/python

file = open("temperatures.txt",'w')

temperatures=[10,-20,-289,100]

def cel2far(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9 / 5 + 32
        return float(f)

for t in temperatures:
    temperature = cel2far(t)
    if temperature.isInt():
    	file.write(str(temperature))

file.close()
