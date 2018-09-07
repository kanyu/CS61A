# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 20:06:45 2018

@author: Kan
"""

#def f(a, b, c, d, e):
#    print(a, b, c, d, e)
#    
#f(5,4,3,2,1)
#
#def g(b,c,d,e):
#    f(6,b,c,d,e)
#    
#g(1,2,3,4)

#Simple Function 
def func(a ,b, c, d, e, f, g = 100):
    print(a ,b, c, d, e, f, g)
    

from functools import partial
#f is the "curried" version of func.
f = cur(func)

c1 = f(1)
c2 = c1(2, d = 4)               # Note that c is still unbound
c3 = c2(3)(f = 6)(e = 5)        # now c = 3
c3()                            # forces the evaluation     <====
                                #   it prints "1 2 3 4 5 6 100"
c4 = c2(30)(f = 60)(e = 50)     # now c = 30
c4()                            # forces the evaluation     <====
                                #   it prints "1 2 30 4 50 60 100"