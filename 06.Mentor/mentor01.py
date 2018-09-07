# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:59:23 2018

@author: Kan
"""

def is_div_4(n):
    if n % 4 == 0:
        return True
    else:
        return False
    
def is_leap_year(n):
    if is_div_4(n):
        return True
    else:
        return False
    
def fizzbuzz(n):
    def fizz(n):
        if n % 3 == 0:
            return True
    def buzz(n):
        if n % 5 == 0:
            return True
    i = 1
    while i <= n:
        if fizz(i) and buzz(i):
            print ('fizzbuzz')
        elif buzz(i):
            print('buzz')
        elif fizz(i):
            print('fizz')
        else:
            print(i)
        i += 1