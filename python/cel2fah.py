# Coding Exercise 1
# Section 3, Lecture 26

def cel2fah(celsius):
    fahrenheit = celsius * 9/5 + 32 #9/5 can be replaced with 1.8
    return(fahrenheit)

f = input("Set a value in Celsius: ")
print(cel2fah(int(f)))
