#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:14:51 2017

@author: deepanshparab
"""

'''
Let's work with numbers.

You are given an array of numbers (floats). You should find the difference between the maximum and minimum element. Your function should be able to handle an undefined amount of arguments. For an empty argument list, the function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. So we should check the result with ±0.001 precision.
Think about how to work with an arbitrary number of arguments.

Input: An arbitrary number of arguments as numbers (int, float).

How it is used: Here you will learn about passing an undefined amount of arguments to functions.

Precondition: 0 ≤ len(args) ≤ 20
all(-100 < x < 100 for x in args)
all(isinstance(x, (int, float)) for x in args)

Your vote gains more value as you grow in level. Starting at level 5 you can upvote a publication twice and starting at level 14, you can upvote something five times!

Output: The difference between maximum and minimum as a number (int, float).
'''


def max1(arg1, arg2):
    if arg1 > arg2: return arg1
    else: return arg2

def min1(arg1, arg2):
    if arg1 < arg2: return arg1
    else: return arg2
    
def checkio(*args):
    if len(args) > 1:
        max = args[0]
        min = args[0]
        for i in range(0,len(args)):
            max = max1(max,args[i])
            min = min1(min,args[i])
        
        return( max- min)
    else:
        return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

