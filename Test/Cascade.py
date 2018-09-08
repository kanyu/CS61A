# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 04:05:17 2018

@author: Kan
"""

def cascade(n, depth=0):
    """Visualization for cascade"""
    if n > 0:
        print(' '* depth, 'cascade({})'.format(n))
        cascade(n-1, depth+1)
        print(' ' * depth, 'return')