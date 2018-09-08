# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:25:39 2018

@author: Kan
"""

def sum_digits(n):
    """
    recursive compute sum of digits of number n
    >>> sum_digits(18)
    >>> 9
    """
    if n // 10 == 0:
        return n
    return n % 10 + sum_digits(n // 10)

#print number from 1 to n
def count_up(n):
    """
    recursive print from 1 to n
    >>> count_up(3)
    >>> 1
    >>> 2
    >>> 3
    """
    if n == 1:
        print(1)
    else:
        count_up(n - 1)
        print(n)


# The Luhn Algorithm
A = [1, 2, 3, 4 ,5]
B= [6, 7, 8, 9 ,10]
def dif_array(A,B):
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return abs(A[0] - B[0])
    elif len(A) != 1:
        return abs(A[0] - B[0]) + dif_array(A[:len(A)-1],B[:len(B)-1])
    
dif_array(A,B)