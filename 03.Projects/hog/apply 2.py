# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 02:12:30 2018

@author: Kan
"""

def apply_2(f):
    return f(f)

def square(x):
    return x*x

d = apply_2(square)
d(3)
