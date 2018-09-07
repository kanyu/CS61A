# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:42:33 2018

@author: Kan

Q0
    a/ 
        What do lambda expression do: Create a function
        Can we write all functions as lambda expressions? No
        In what case are lambda expressions useful? Pass as agurment /
                                                    return / short code
    
    b/
        
"""

pow = lambda x, y: x**y
def pow(x, y):
    return x**y

foo = lambda x: lambda y: lambda z: x + y * z

def foo(x):
    def lambda1(y):
        def lambda2(z):
            return x + y * z
    return lambda1

compose = lambda f, g: lambda x: f(g(x))

def compose(f, g):
    def h(x):
        return f(g(x))
    return h

#c)​ Challenge:​ Complete the given lambda expression so the second line 
#evaluates to 2018. You may only use the names two_thousand, two, k, eight, 
#and teen and parentheses in your expression 
#(no numbers, operators, etc.). Hint: an environment diagram might be useful.

#best_year = lambda four: lambda k:
#best_year(9)(lambda eight: lambda teen: 2000 + eight + teen)
    
def make_skipper(n):
    """
    >>> a = make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    skip = lambda k: k % n
    def _print(a):
        i = 0
        while i <= a:
            if skip(i):
                print(i)
            i += 1
    return _print

def make_alternator(f, g):
    """
    >>> a = make_alternator(lambda x: x * x, lambda x: x + 4)
    >>> a(5)
    1
    6
    9
    8
    25
    >>> b = make_alternator(lambda x: x * 2, lambda x: x + 2)
    >>> b(4)
    2
    4
    6
    6
    """
    def alter(x):
        for i in range(x+1):
            if i > 0 and i % 2 == 0:
                print(g(i))
            elif i > 0:
                print(f(i))
    
    return alter

#reverse list recusive

def reverse(lst):
    if len(lst) <= 1:
        return lst
    rest = lst[1:]
    first = [lst[0]]
    return reverse(rest) + first
    
lst = ['a', 'b', 'c', 'd', 'e']
rev = reverse(lst)

#    Write combine_skipper, which takes in a function f and list lst 
#    and outputs a list. When this function takes in a list lst, 
#    it looks at the list in chunks of four 
#    and applies f to the first two elements in every set of four elements 
#    and replaces the first element with the output of the function f 
#    applied to the two elements as the first value and the index of the 
#    second item of the original two elements as the second value 
#    of the new two elements. f takes in a list and outputs a value. 
#   [Assume the length of lst will always be divisible by four]

def combine_skipper(f, lst):
    """
    >>> lst = [4, 7, 3, 2, 1, 8, 5, 6]
    >>> f = lambda l: sum(l)
    >>> lst = combine_skipper(f, lst)
    >>> lst
    [11, 1, 3, 2, 9, 5, 5, 6]
    >>> lst2 = [4, 3, 2, 1]
    >>> lst2 = combine_skipper(f, lst2)
    >>> lst2
    [7, 1, 2, 1]
    """
    n = 0
    while n < len(lst):
        if n % 4 == 0:
            l = lst[n:n+2]
            lst[n] = f(l)
            lst[n + 1] = n + 1
        n += 1
    return lst

lst = [4, 7, 3, 2, 1, 8, 5, 6]
f = lambda l: sum(l)
lst = combine_skipper(f, lst)
print(lst)
 
lst2 = [4, 3, 2, 1]
lst2 = combine_skipper(f, lst2)
print(lst2)


# Three things in every recursive function ?
# 1. Base case
# 2. Recursive calls
# 3. Use recursive calls to solve problem

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(5))

def cascade2(n):
    print(n)
    if n >= 10:
        cascade2(n // 10)
        print(n)
        
#cascade2(235252353)

def mystery(n):
    """
    sum of zero to n
    """
    if n == 0:
        return 0
    else:
        return n + mystery(n - 1)

def fooo(n):
    """
    return 0
    """
    if n < 0:
        return 0
    return fooo(n - 2) + fooo(n - 1)

def fooply(n):
    if n < 0:
        return 0
    return fooo(n) + fooply(n - 1)

def has_seven(k):
    """ True if have 7
    """
    if k < 7:
        return False
    elif k % 10 == 7:
        return True
    elif k % 10 != 7:
        return has_seven(k // 10)
    
#    Implement the combine function, which takes a non-negative integer n, a two-argument function
#    f, and a number result. It applies f to the first digit of n and the result of combining the rest of the
#    digits of n by repeatedly applying f (see the doctests). If n has no digits (because it is zero),
#    combine returns result. Assume n is non negative.
from operator import add, mul
def combine (n , f , result ):
    """
    Combine the digits in n using f.
    >>> combine (3, mul, 2) # mul (3, 2)
    6
    >>> combine (43, mul, 2) # mul (4, mul (3, 2))
    24
    >>> combine (6502, add, 3) # add (6, add (5, add (0, add (2 , 3)))
    16
    >>> combine (239, pow, 0) # pow (2, pow (3, pow (9, 0)))
    8
    """
    if n == 0:
        return result
    else:
        return combine(n // 10, f, f(n % 10, result))




