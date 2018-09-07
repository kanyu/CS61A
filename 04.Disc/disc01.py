# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:37:59 2018

@author: Kan
"""

#Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
#Write a function that takes in the current temperature and a boolean value telling
#if it is raining and returns True if Alfonso will wear a jacket and False otherwise.
#First, try solving this problem using an if statement.
#    def wears_jacket_with_if(temp, raining):
#    """
#    >>> wears_jacket(90, False)
#    False
#    >>> wears_jacket(40, False)
#    True
#    >>> wears_jacket(100, True)
#    True
#    """

def wears_jacket(temp, raining):

    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    
    if temp < 60 or raining == True:
        return True
    else:
        return False
    
square = lambda x : x * x



# Is prime ?
def is_prime(n):
    """ determine if n is a prime or not"""
    k = n - 1
    while k > 1:
        if n % k == 0:
            return False
        k -= 1
    return True

def is_even(n):
    return n % 2 == 0


def keep_ints(cond, n):
    """ print numbers match the condition input function"""
    i = 0
    while i < n:
        if is_even(i):
            print(i)
        i += 1
        
def outer(n):
    def inner(m):
        return n - m
    return inner


def keep_ints2(n):
    """ print numbers match the condition input function"""
#    m = n
    def condition(cond):
        i = 0
        while i < n:
            if cond(i):
                print(i)
            i += 1
    return condition
        
    
        
    