# Coding Exercise 1
# Section 3, Lecture 26

def cel2fah(celsius):
    fahrenheit = celsius * 9/5 + 32 #9/5 can be replaced with 1.8
    return(fahrenheit)

c = float(input("Set a value in Celsius: "))

if c < -273.15:
    print("The lowest possible temperature that physical matter can reach is -273.15C")
else:
    print ("Celsius value set to: ", c)
    print ("Fahrenheit value is: ", cel2fah(c))
