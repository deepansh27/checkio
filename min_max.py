#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:28:11 2017

@author: deepanshparab
"""

def simple_max(arg1,arg2,key):
    if key!=None:
        if key(arg1)==key(arg2): 
            return arg1
     
        elif key(arg1)>key(arg2):
            return arg1
        else:
            return arg2
    if key == None:
         if arg1>arg2: 
            return arg1
         else:
            return arg2
     
       
        

def simple_min(arg1,arg2,key):
       if key!=None:
           if key(arg1)==key(arg2):
               return arg1
     
           elif key(arg1)<key(arg2):
               return arg1
           else:
               return arg2
       if key == None:
           if arg1<arg2: 
               return arg1
           else:
               return arg2
        
def max(*args,**kwargs):
    key = kwargs.get("key",None)
#    print(key)
    if len(args) == 1:
        args = list(args[0])
    
    max1 = args[0]
    for i in range(0,len(args)):
        max1= simple_max(max1,args[i],key)
    return (max1)


    
def min(*args,**kwargs):
    key = kwargs.get("key",None)
    if len(args) == 1:
        args = list(args[0])
    
    min1 = args[0]
    
    for i in range(0,len(args)):
        min1= simple_min(min1,args[i],key)
    return min1
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

