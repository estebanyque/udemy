#!/usr/bin/python

print("Celsius value 5")


def cel2far(c):

    if c < -273.15 :
        print("Error, value out of range")
        return
    else:
        f = c * 9 / 5 + 32
        return f

print("Fahrenheit=" + str(cel2far(-274)))