"""Lab 2: Lambda Expressions and Higher Order Functions"""

# Lambda Functions
from operator import add

def curry2(func):
    def adder(x):
        def addit(y):
            return func(x, y)
        return addit
    return adder

#curried_add = curry2(add)
#add_three = curried_add(3)
#add_three(5)

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"
    adder = lambda x: lambda y: func(x, y)
    return adder

#lambda_curried_add = lambda_curry2(add)
#add_3 = lambda_curried_add(3)
#r = add_3(5)
    
#Q4 Composite Identity Function
    
#add_one = lambda x: x + 1
#square = lambda x: x * x
#mul_three = lambda x: x * 3

def compose1(f, g):
    return lambda x: f(g(x))

#a1 = compose1(square, add_one)
#a2 = compose1(mul_three, a1)
def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    def h(x):
        if f(g(x)) == g(f(x)):
            return True
        else:
            return False
    return h

#b1 = composite_identity(square, add_one)
    

#Q5 Count van Count

def count_factors(n):
    i, count = 1, 1
    while i < n:
        if n % i == 0:
            count += 1
        i += 1
    return count

def is_prime(n):
    return count_factors(n) == 2

def count_cond(condition):
    def cond(n):
        i, count = 1, 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return cond


    