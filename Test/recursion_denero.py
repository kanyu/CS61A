# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:39:03 2018

@author: Kan
"""

def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
    
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last
    
def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
    
#Luhn Algorithm my approach using single recursion function
        
luhn_check = [False]
def luhn_sum_2(n):
    if n < 10:
        return n
    the_last, the_rest =  n % 10, n // 10
    if luhn_check[0]:
        luhn_check[0] = False
        return sum_digits(2 * the_last) + luhn_sum_2(the_rest)
    else:
        luhn_check[0] = True
  
        return the_last + luhn_sum_2(the_rest)

# using list property and method to calculate luhn sum    

def sum_list(L):
    """
    Sum of a positive list
    """
    if len(L) == 1:
        return int(L[0])
    return int(L.pop())+ sum_list(L)

def luhn_sum_3(n):
    """
    using list property and method to calculate luhn sum
    """
    n = str(n)
    luhn_digits = [sum_digits(int(d) * 2) for d in n[-2::-2]]
    normal_digits = [int(d) for d in n[::-2]]
    return sum_list(luhn_digits) + sum_list(normal_digits) 

# ODD AND EVEN
    
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

# to think in recursive way remember: 
# I CAN SOLVE THE PROBLEM IF I KNOW THE SOLUTION OF PREVIOUS CASE
# FEED the previous question into the same function itself till the base case 
# You just need to solve the simplest case. the rest just 
# let the computer ask back to the simplest case


def md(n):
    if n < 10:
        return n
    return (n % 10) * md(n // 10)

def pow(n, k):
    if k == 1:
        return n
    return n * pow(n, k - 1)

def count8(n):
    if n == 8:
        return 1
    elif n < 10:
        return 0
    else:
        if n % 10 == 8:
            return 1 + count8(n // 10)
        else:
            return 0 + count8(n // 10)

#def is_prime(n):
#    
#    if n == 1  or n == 2:
#        return True
#    elif not(0 + (is_prime(n % (n - 1)))):
#        return True
#    else:
#        return False
        
def is_prime(n):
    k = n - 1
    if n == 1 or n == 2:
        return True
    else:
        while k > 1:
            if n % k == 0:
                return False
            k -= 1
    return True

def count_prime(n):
    if n == 1:
        return 1
    elif n == 2: 
        return 2
    else:
        if is_prime(n):
            return 1 + count_prime(n - 1)
        else:
            return 0 + count_prime(n - 1)
        

def sum_range(lst, i, j):
    if i > j:
        return 0
    elif i == j:
        return lst[i] # or lst[j]
    return lst[i] + sum_range(lst, i + 1, j)

def sum_range_2(lst, i, j):
    if i > j:
        return 0
    return lst[i] + sum_range_2(lst, i + 1, j)

def can_win(n):
    if n < 0:
        return False
    elif n <= 3:
        return True
    else:
        return

def player_1(s):
    return player_2(s - 1)

def player_2(s):
    return player_1(s - 1)
















