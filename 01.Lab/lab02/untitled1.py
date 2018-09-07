# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 06:29:01 2018

@author: Kan
"""

i = 1
k = 4
def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3
f1 = add1
f2 = times2
f3 = add3
x = 1
if k == 0:
#    print("0", x)
else:
    while i <= k:
        if (i == 1 or i % 3 == 1) and i <= k:
            x = f1(x)
            i += 1
#            print(i, x)
        if (i == 2 or i % 3 == 2) and i <= k:
            x = f2(x)
            i += 1
#            print(i, x)
        if (i == 3 or i % 3 == 0) and i <= k:
            x = f3(x)
            i += 1
#            print(i, x)