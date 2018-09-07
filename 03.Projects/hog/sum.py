# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:40:58 2018

@author: Kan
"""

def sum_naturals(n):
    total = 0
    k = 1
    while k <= n:
        total = total + k
        k = k + 1
    return total

sum_naturals(100)


def sum_square(n):
    total = 0
    k = 1
    while k <= n:
        total = total + k**2
        k = k + 1
    return total

sum_square(100)

# pi_sum formula: Sum(k=1->n) of 8/(4k-3)(4k-1)
def pi_sum(n):
    total = 0
    k = 1
    while k<= n:
        total = total + 8/((4*k-3)*(4*k-1))
        k = k + 1
    return total

pi_sum(100)

def sum_term(n,term):
    total = 0
    k = 1
    while k<=n:
        total += term(k)
        k += 1
    return total


def square(x):
    return x*x

def pii(x):
    return 8/(4*x-3)/(4*x-1)

sum_term(100,square)

def sum_square_v2(n):
    return sum_term(n,square)


#    Function as general method:
#    Example: A function to improve guess result from an update
#    function depend on how is close to a close function
#    def improve(update, close, guess = 1):
#        while not close(update):
#            guess = update(guess)
#        return guess
    
def improve(update, close, guess = 1):
    while not close(update):
        guess = update(guess)
    return guess

def update_guess_phi(guess):
    return 1/guess + 1

def square_close_to_phi(guess):
    return approx_eq(guess**2, guess + 1)

def approx_eq(x,y, tolerance = 1e-15):
    return abs(x -y) <= tolerance


# newton update
    
def newton_update(f,df):
    def update(x):
        return x - f(x)/df(x)
    
def find_zero(f,df):
    def near_zero(x):
        return approx_eq(f(x),0)
    return improve(newton_update(f,df),near_zero)













































