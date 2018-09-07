# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:49:48 2018

@author: Kan
"""

#Mul recursion

def recur_mul(n, m):
    if m == 1:
        return n
    else:
        return n + recur_mul(n, m - 1)
    
#count down print
        
def count_down(n):
    if n == 1:
        print(1)
    else:
        print(n)
        count_down(n - 1)
        
def count_up(n):
    def helper(i):
        if i == n:
            print(n)
        else:
            print(i)
            helper(i + 1)
    helper(1)
        
def count_stair_ways(n, x, y):
    """
    I want to go up a flight of stairs that has n steps. 
    I can either take x or y steps each time. 
    How many different ways can I go up this flight of stairs?
    Write a function count_stair_ways that solves this problem for me. 
    Assume n is positive.
    Before we start, what’s the base case for this question? 
    What is the simplest input?
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return count_stair_ways(n - x, x, y) + count_stair_ways(n - y, x, y)
    
#def count_stair_1_2(n):
#    if n < 0:
#        return 0
#    if n == 1:
#        return 1
#    else:
#        return count_stair_1_2(n - 1) + count_stair_1_2(n - 2)
        
#def count_k(n, k):
#    if n < 0 :
#        return 0
#    if n == 0:
#        return 1
#    if k == 0:
#        return 0
#    else:
#        return count_k(n-k, k) + count_k(n, k-1)
#geek for geek way    
def countWaysUtil(n,m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i<=m and i<=n:
        res = res + countWaysUtil(n-i, m)
        i = i + 1
    return res
  
def countWays(s,m):
    return countWaysUtil(s+1, m)
     
 
# Driver program
a = countWays(10, 10)

#my way

def count_stair(n, m):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        total = 0
        i = 1
        while m - i > 0:
            total += count_stair(n, m - i)
            i += 1
        return count_stair(n - m, m) + total
    
#official way:
def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total_ways = 0
        i = 1
        while i <= k:
            total_ways += count_k(n - i, k)
            i += 1
        return total_ways
        
def count_sum_f(n, f, m):
    """ Return the number of ways that n can be partitioned into
    unique positive values obtained by applying the shrinking
    function f repeatedly to m
    >>> count_sum_f(6, lambda k: k - 1, 4) # 4+2, 3+2+1
    2
    >>> count_sum_f(12, lambda k: k - 2, 12) # 12, 10+2, 8+4, 6+4+2
    4
    >>> count_sum_f(11, lambda k: k // 2, 8) # 8 + 2 + 1
    """
    if n == 0:
        return 1
    elif n < 0 or m <= 0:
        return 0
    else:
        return count_sum_f(n - m, f, f(m)) + count_sum_f(n, f, f(m))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    