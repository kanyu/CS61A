# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:38:28 2018

@author: Kan
"""

def tree(label, branches=[]):
    # returns a Tree of some form
    return True
    
def label(tree):
    # returns the label of your root node in the Tree
    return True

def branches(tree):
    # returns the branches in your Tree
    return True
    
def is_leaf(tree):
    # tells you if a node is a leaf or not
    return True
    

def cascade(n):
    i = 1
    def grow(i):
        print(i)
        if i < n:
            grow(i+1)
    
    def shrink(n):
        print(n)
        if n >= i:
            shrink(n-1)
    grow(1)
    print(n)
    shrink(n)
            