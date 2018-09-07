# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 17:59:16 2018
calculate Sum of Square, Cube, Pi sequence
@author: Kan
"""
from math import *

def square(x):
    return x*x

def cube(x):
    return x*x*x

def pie(x):
    return pi
    

def make_log_base(n):
    def log_base(x):
        return log(x, n)
    return log_base