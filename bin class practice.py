# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:03:25 2018

@author: takyon
"""
class Container:
    pass

class Bin(Container):
    
    def __init__(self, volume,):
        self.volume=volume
        self.things_list=[]
        
    def change_volume(self, new_volume):
        self.volume=new_volume
        
    
    def get_volume(self):
        return self.volume
    
    def put_object(self, thing):
        self.things_list.append(thing)
        
    def get_things(self):
        return self.things_list

class Bag(Container):
    
    
    def __init__(self, volume):
        self.volume=volume
        self.things_list=[]
        
    def change_volume(self, new_volume):
        self.volume=new_volume
        
    
    def get_volume(self):
        return self.volume
    
    def put_object(self, thing):
        self.things_list.append(thing)
        
    def get_things(self):
        return self.things_list
            

    
class Trash(object):
    def __init__(self, size):
        self.size=size
    
    def put_trash(self, Container):
        if self.size > Container.get_volume():
            print("Trash is too big")
        else:
            Container.put_object(self)
        
money=Trash(1)

big_bag=Bag(5)        