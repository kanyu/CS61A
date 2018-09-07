# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:28:34 2018

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
    return lambda y: f(x, y)

def fox_says(start, middle, end, num):
    
    def repeat(k):
        if k == 1:
            return middle 
        else:
            return repeat(k - 1) + '-' + middle
        
    return start + '-' + repeat(num) + '-' + end

#(lambda x: lambda y:_____)(lambda f: f())(lambda z: z * z)() #evaluate to 9
    
def combine(n, f, result):
    """
    Combine the digits in non-negative integer n using f.
    >>> combine(3, mul, 2) # mul(3, 2)
    6
    >>> combine(43, mul, 2) # mul(4, mul(3, 2))
    24
    >>> combine(6502, add, 3) # add(6, add(5, add(0, add(2, 3)
    )))
    16
    >>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0))))
    8
    """
    if n == 0:
        return result
    else:
        return combine(n // 10, f, f(n % 10, result))
    
#    . James wants to print this week’s discussion handouts for all the students in CS
#    61A. However, both printers are broken! The first printer only prints multiples of n
#    pages, and the second printer only prints multiples of m pages. Help James figure out
#    whether or not it’s possible to print exactly total number of handouts!

def has_sum(total, n, m):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 0 * 3 + 1 * 5 = 5
    True
    >>> has_sum(11, 3, 5) # 2 * 3 + 1 * 5 = 11
    True
    """
# have not solve yet
    if n < m:
        n, m = m, n
    if total < n and total < m:
        return False
    elif total == n or total == m:
        return True
    return has_sum(total - n, n, m)


def kbonacci(n, k):
    """ Return element N of K-bonacci sequence.
    >>> kbonacci(3, 4)
    1
    >>> kbonacci(9, 4)
    29
    >>> kbonacci(4, 2)
    3
    >>> kbonacci(8, 2)
    21
    """
    if n < k - 1:
        return 0
    elif n == k - 1:
        return 1
    else:
        total = 0
        i = 0
        while i < n:
#            total = total + # unsolve kbonacci(n - 1, k)
            i = i + 1
        return total
    

            
    