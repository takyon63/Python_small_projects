# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:38:43 2018

@author: takyon
"""

#Guessing Game One

secret=print("Please choose number from one to nine: ")
high=9
low=1
middle=(high+low)//2
num_guesses=0
print("Please choose number from one to nine: ")
while secret!="exit":
    num_guesses+=1

    guess=input("Is your number {0}? Press c if correct, h if too high, l if too low.  ".format(middle))
    if guess == "c":
        print("Thank you for playing, it took only {0} guesses".format(num_guesses))
        cont_or_not=input("Do you want to play another one, type exit to exit, and start to start a new game:  ")
        if cont_or_not=="start":
            high=9
            low=1
            middle=(high+low)//2
            continue
        else:
            print("Thank you for playing, it took only {0} guesses".format(num_guesses))
            break
        
    elif guess == "h":
        high=middle
        middle=(high+low)//2
        
    elif guess == "l":
        low=middle
        middle=(high+low)//2
        
    elif guess == "exit":
        print("Thank you for playing, it took only {0} guesses".format(num_guesses))
        break