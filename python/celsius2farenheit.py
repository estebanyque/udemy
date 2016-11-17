#!/usr/bin/python
print("Celsius value 5")


def cel2far(c):

    f = c * 9 / 5 + 32
    return f

print("Fahrenheit=" + str(cel2far(5)))