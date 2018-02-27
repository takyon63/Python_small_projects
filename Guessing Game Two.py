# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:38:43 2018

@author: takyon
"""

#Guessing Game One
import random

while True:
    num_guesses=0
    rn=str(random.randint(1,10))
    
    while True:
        num_guesses+=1
        guess=input("Please guess number: ")
        if rn > guess:
            print("Your guess is too low")
        elif rn< guess:
            print("Your guess is too high")
        else:
            print ("Correct! It took you only {0} guesses".format(num_guesses))
            break
        
    cont=input("Do you want to continue play? Type exit to exit, any other key to continue. ")
    if cont=="exit":
        break
    else:
        continue
