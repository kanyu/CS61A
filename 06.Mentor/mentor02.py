# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:11:29 2018

@author: Kan
"""

def mystery(f, x):
    """
    >>> from operator import add, mul
    >>> a = mystery(add, 3)
    >>> a(4) # add(3, 4)
    7
    >>> a(12)
    15
    >>> b = mystery(mul, 5)
    >>> b(7) # mul(5, 7)
    35
    >>> b(1)
    5
    >>> c = mystery(lambda x, y: x * x + y, 4)
    >>> c(5)
    21
    >>> c(7)
    23
    """
    def helper(y):
        return f(x, y)
    return helper
    

# Write a function duplicate_list, 
# which takes in a list of positive integers 
# and returns a new list with
# each element x in the original list duplicated x times.

def duplicate_list(lst):
    """
    >>> duplicate_list([1, 2, 3])
    [1, 2, 2, 3, 3, 3]
    >>> duplicate_list([5])
    [5, 5, 5, 5, 5]
    """
    duplist = []
    for e in lst:
        for _ in range(e):
            duplist.append(e)
    
    return duplist
    
