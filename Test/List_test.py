# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:11:43 2018

@author: Kan
"""
L = [1, 2, 3, 4, 5]
def rev(h):
    """Reverses L in place (i.e. doesn't create new lists).

    >>> L = [1, 2, 3, 4]
    >>> reverse(L)
    >>> L
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"   
    l = h[::-1]
    i = 0
    while i <= len(h)-1:
        h[i] = l[i]
        i += 1

def map_mut(f, L):
    """Mutatively maps f onto each element in L.

    >>> L = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(L)):
        L[i] = f(L[i])

map_mut(lambda x: x**2, L)    