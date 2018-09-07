"""Lab 1: Expressions and Control Structures"""

# Coding Practice
def square(x):
    return x * x

def opposite(x):
    return not x

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
#    def f_holder(fx):
#        fx = f(x)
#        return fx
#    while n > 0:
#        f_holder = f_holder(f_holder)
#        n -= 1
#    return f_holder()
    def rfun(p):
        acc = p
        i = n
        while i > 0:
            acc = f(acc)
            i -= 1
        return acc
    return rfun(x)

def repeated2(f, n, x):
    def rfun(p):
        acc = p
        i = n
        while i > 0:
            acc = f(acc)
            i -= 1
        return acc
    rfun(x)  # no return keyword so repeated2 return value = None !!!

def repeated3(f, n, x):
    while n > 0:
        x = f(x)
        print(x)
        n -= 1
    return x
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    total = 0
    num_to_string = str(n)
    for i in num_to_string:
        total += int(i)
    return total

def sum_digits_2(n):
    total = 0
    i = len(str(n))
    while i > 0:
        total = total + n % 10
        n = n // 10
        i -= 1
    return total
    
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    count = 0
    i = len(str(n))
    while i > 0:
        if n % 10 == 8:
            count += 1
            n = n // 10
            i -= 1
            if count == 2:
                return True
        else:
            n = n // 10
            count = 0
            i -= 1
    return False

# Question 6 -> 7 use ok
    
# Question 8: Fix the Bug
    

    

