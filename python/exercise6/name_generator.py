#!/usr/bin/python

import random, string

message="What letter do you want? 'v' for vowels, 'c' for consonants, 'l' for any letter: "

letter_input1 = input(message)
letter_input2 = input(message)
letter_input3 = input(message)

vowels='aeiou'
consonants='bcdfghjklmnpqrstvwxyz'
letters=string.ascii_lowercase

#print(letter_input1, letter_input2, letter_input3)

def generator(choice):
    if choice == 'v':
        return(random.choice(vowels))
    elif choice == 'c':
        return(random.choice(consonants))
    elif choice == 'l':
        return(random.choice(letters))
    else:
        return(choice)

for i in range(20):
    name = generator(letter_input1) + generator(letter_input2) + generator(letter_input3)
    print(name)
