# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:27:54 2018

@author: Kan
"""

def search(f):
    x = 0
    while True:
        if f(x):
            print(x)
            return x
        x += 1
        
def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def fall(x):
    
    return True