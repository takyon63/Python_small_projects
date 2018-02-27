# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:20:10 2018

@author: takyon
"""

filename=input("Enter a file name:")
with open(filename) as f:
    text=f.read()
    
        
def countchar(text,char):
    count=0
    for letter in text:
        if letter==char:
            count+=1
    return count


for char in 'abcdefghijklmnopqrstuvwxyz':
    perc=100*(countchar(text,char)/len(text))
    #print(countchar(text,char))
    #print(len(text))
    print('{0}-{1}%'.format(char,round(perc,2)))

