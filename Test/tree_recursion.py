# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:14:19 2018

@author: Kan
"""

def cascade(n):
    """
    print out a cascading tree of a positive integer n.
    >>> cascade(486)
    486
    48
    4
    48
    486
    """
    if (n) < 10:
        print (n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
        
def cascade_2(n):
        print (n)
        if n > 10:
            cascade(n // 10)
            print(n)
        
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
    
def fib_iter(n):
    prev, cur = 0, 1
    if n == 0:
        return 0
    while n > 1:
        prev, cur = cur, prev + cur
        n -= 1
    return cur

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m,m)\
        + count_partitions(n, m-1)
        
# 100c from 50c ,25c, 10c, 5c, 1c
L = [0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
def change_money(n, L):
    def _change(n, m, i):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            cur = L[len(L)- i - 1]
            nex = L[len(L)- i - 2]
            return _change(n-cur,cur, i) + _change(n, nex, i + 1)   
    return _change(n, L[len(L)- 1], 0)

#d = count_partitions(5, 4)
#c = change_money(5000, L)
