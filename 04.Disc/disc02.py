# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

is_even = lambda n: n % 2 == 0
is_odd = lambda n: not is_even(n)

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 0
    while i <= n:
        if cond(i):
            print (i)
        i += 1
        
def keep_ints2(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(5)(is_even)
    2
    4
    """
    def cond(f):
        i = 0
        while i <= n:
            if f(i):
                print (i)
            i += 1
    return cond

