# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:06:27 2018

@author: takyon
"""

mydict= {}

list1=['apple', 'orange', 'cherry', 'lemon', 'tangerine','apple']

for i in list1:
    if i in mydict:
        mydict[i]+=1
    else:
        mydict[i]=1 
        
        
def remove_dup(dictionary):
    dictcopy=dictionary.copy()
    for i in dictionary:
        if dictionary[i]>1:
            dictionary[i]-=1
            
    return dictcopy
remove_dup(mydict)
print(mydict)