#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:13:43 2017

@author: deepanshparab
"""
def safe_pawns(pawns):
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1  #selects the first element of the 
        print('row:'+str(row))
        col = ord(p[0]) - 97  # ord() returns the ascii value of the char so we get 0 for a, 2 for b by subtracting 97 from it i.e the value of col
        print('col:'+str(col))
        pawns_indexes.add((row, col)) #insert it into a set by using .add()
    count = 0
    for row, col in pawns_indexes:
        is_safe = any(((row - 1, col - 1) in pawns_indexes, (row - 1, col + 1) in pawns_indexes))
        if is_safe:
            count += 1
    return count
        

     

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")



