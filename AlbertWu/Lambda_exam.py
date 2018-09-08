# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 19:56:48 2018

@author: Kan
"""

#   ALBERT WU
"""
Question 1
Fill in the blanks for the following expression so that result is the number 42.
"""
x = lambda x, y: lambda: x - y
result = (lambda one, question: one(46, question)())(x, 4)

"""
Question 2
Fill in the blanks for the following expression so that result is the boolean True.
"""
x = lambda x: lambda y: x(y)
result = (lambda fair, dice: x(fair)(dice))(lambda fair: fair == 3, 3)

"""
Fill in the blanks for the following expression so that each call to mapper prints the output displayed below:

>>> def mapper(fn, num):
...     i = 0
...     while i < num:
...         print(fn(i))
...         i = i + 1
>>> mapper(lambda x: ______, 4)
1
3
5
7
>>> mapper(lambda x: ______, 5)
-2
-1
0

1
2
>>> mapper(lambda x: ______, 5)
0
-1
1
-2
2
"""

"""
Environment Diagrams
"""
# Question 3
f = lambda x: lambda y: lambda z: g(x + y + z)

g = f(3)
f(4)(5)(6)

# Question 4
fn = lambda f, a: f(f(2*a))
result = fn(lambda x: x*x, 2)

# Question 5
fn = lambda: lambda: print('hi')

def example(x):
    print('example')
    return x

result = example(fn())()


#    ============================= FA14MT1 ====================================
"""
    4. (6 points) Lambda at Last

    (a) (2 pt) Fill in the blank below with an expression so that the second line evaluates to 2014. 
    You may only use the names two_thousand, two, k, four, and teen and parentheses in your expression 
    (no numbers, operators, etc.).
"""
two_thousand = lambda two: lambda k: __________________________________________ 
two_thousand(7)(lambda four: lambda teen: 2000 + four + teen)

"""
    (b) (4 pt) The if_fn returns a two-argument function that can be used to select among alternatives, 
    similar to an if statement. Fill in the return expression of factorial so that it is deﬁned correctly 
    for non-negative arguments. You may only use the names 
    if_fn, condition, a, b, n, factorial, base, and recursive and parentheses in your expression 
    (no numbers, operators, etc.).
"""

def if_fn(condition): 
    if condition: 
        return lambda a, b: a 
    else: 
        return lambda a, b: b
    
def factorial(n): 
    """Compute N! for non-negative N. N! = 1 * 2 * 3 * ... * N.
    >>> factorial(3) 6 >>> factorial(5) 120 >>> factorial(0) 1 
    """ 
    def base(): 
        return 1 
    def recursive(): 
        return n * factorial(n-1)
    return ____________________________________________________________________



#    ============================= SP15MT1 ====================================

"""    
    (b) (3 pt) Add parentheses and single-digit integers in the blanks below 
    so that the expression on the second line evaluates to 2015. You may only add 
    parentheses and single-digit integers. You may leave some blanks empty.
"""

lamb = lambda lamb: lambda: lamb + lamb
lamb(1000)______ + (lambda b, c: b______ * b______ - c______)(lamb(______), 1)______


#    ============================= FA15MT1 ====================================

"""
    (2 pt) Write a number in the blank so that the ﬁnal expression below evaluates to 2015. 
    Assume decompose1 is implemented correctly. 
    The make_adder and compose1 functions appear on the left column of page 2 of your study guide.
"""

e, square = make_adder(1), lambda x: x*x
decompose1(e, compose1(square , e))(3) + ______________________________________



#    ============================= SP18MT1 ====================================

"""
    (c) (2 pt) Complete the expression below by only adding parentheses 
    so that the whole expression evaluates to 2018. 
    Each blank should be ﬁlled with one or more parentheses.
"""

(lambda a, x: x + (lambda y: lambda z: y+z+1000)(1000 _____ 10 _____ 5, _____ lambda: 8 _____ )



























