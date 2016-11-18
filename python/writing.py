#!/usr/bin/python

file = open("example.txt", 'w')
file.write("New line!")
file.close()

file = open("example.txt", 'a') #append
lst = ["cuatro\n","cinco\n"]
for i in lst:
    file.write(i)

file.close()

# a : agregar al final
# a+ : agregar al final y cren lectura, crea el archivo si no existe
# r : lectura
# r+ : lectura y escritura
# w : solo escrutura, sobreescribe si el archivo existe, lo crea de lo contrario
# w+ : lectura y escritura, sobre escribe el archivo, crea uno nuevo
