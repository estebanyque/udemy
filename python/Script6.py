#/usr/bin/python

#planet = input("What planet are you from?")
#print(planet)

password=''

while password != 'python123':
    password = input('Enter your password: ')
    if password=='python123':
        print("You are logged in!")
    else:
        print("Sorry, try again...")