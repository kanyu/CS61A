# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 03:34:49 2018

@author: Kan
"""

def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

# Compute the fist ten power of 2
    
def powers_of_2(n):
    i = 0
    while i <= n:
        print (pow(2, i))
        i += 1
        
# Compute n powers of x from a to b
def powers_of_x_from_a_to_b(x, a, b):
    while a <= b:
        print (pow(x, a))
        a += 1

p2f = curried_pow(2)
def powers_of_x_from_a_to_b_2(f, a, b):
    while a <= b:
        print (p2f(a))
        a += 1

def trace(fn):
    print("blah: ", fn, "============")
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped

def prt(fn):
    print("blah: ", fn)
    return fn

@trace
def triple(x):
    return 3 * x

triple(3)