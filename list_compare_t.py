# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:20:15 2018

@author: takyon
"""

import random

list_a =random.sample(range(100),30)
list_b=random.sample(range(100),20)


def compare_lists(list_a, list_b):
    '''Takes in 2 lists of different lenghts,
    outputs one list with same elements'''
    
    compound_list=[]
    
    if len(list_a)>len(list_b):
        big_list=list_a
    else:
        big_list=list_b

    if big_list is list_a:
        small_list=list_b
    else:
        small_list=list_a
    
    for elem in small_list:
        if elem in big_list:
            if elem not in compound_list:
                compound_list.append(elem)
    return compound_list

compare_list