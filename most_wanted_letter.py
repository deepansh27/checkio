#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:43:03 2017

@author: deepanshparab
"""


def checkio(text):
    freqs = {}
    for ch in text:
        if ch.isalpha():
            try:
                freqs[ch.lower()] += 1
            except KeyError:
                freqs[ch.lower()] = 1
    freq_max = max(freqs.items(), key=lambda x: x[1])
    print(type(freq_max))
    print(freq_max)
    for k,v in freqs.items():
        if v == freq_max:
            max_freq_char = k
         
    return sorted(max_freq_char)
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    #assert checkio("AAaooo!!!!") == "a", "Only letters."
    #assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")


    
            
            
    
   
    




