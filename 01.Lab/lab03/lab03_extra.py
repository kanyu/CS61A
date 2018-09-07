""" Optional problems for Lab 3 """

# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    k = n - 1
    flag = [True]
    def _prime(n, k):
        if n == 1 or n == 2 or k == 1:
            return True
        elif n % k == 0:
            flag[0] = False
        else: 
            return _prime(n, k - 1)
    _prime(n, k)
    return flag[0]

def is_prime_2(n):
    return True


# Q5
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a < b:
        a, b = b, a
    def _gcd(a, b):
        if a == b or a % b == 0:
            return b
        return _gcd(b, a % b)
    return _gcd(a, b)


# Q6
def split(n):
    the_last = n % 10
    the_rest = n // 10
    the_next = the_rest % 10
    return the_last, the_next, the_rest

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    Do not use assigment statement

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
# my attemp - fail: do not run, kernel die   
#    the_last, the_next, the_rest = split(n)
#    
#    def count_pair(the_last, the_next, the_rest):
#        if n < 10:
#            return 0
#        elif the_last + the_next == 10:
#            return 1 + count_pair(the_last, (the_rest // 10) % 10, the_rest // 10)
#        elif the_last + the_next != 10:
#            return count_pair(the_last, (the_rest // 10) % 10, the_rest // 10)
#
#    
#    return count_pair(the_last, the_next, the_rest)
    
# OFFICICAL SOLUTION
    if n < 10:
        return 0
    else:
        return ten_pairs(n // 10) + count_digit(n // 10, 10 - n % 10)

def count_digit(n, digit):
    if n == 0:
        return 0
    elif n % 10 == digit:
        return count_digit(n // 10, digit) + 1
    else:
        return count_digit(n // 10, digit)
        

# Q7
def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    "*** YOUR CODE HERE ***"
    
    all_factors = []
    i = n - 1
    def creat_flist(n, i):
        if i == 1:
            return all_factors.append(1)
        elif n % i == 0:
            creat_flist(n, i - 1)
            all_factors.append(i)
        elif n % i != 0:
            creat_flist(n, i - 1)

    creat_flist(n, i)
    return all_factors

    
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """ 
    L = str(n)
    def _palin(L, i = 0):
        j = len(L) - 1
        if len(L) <= 1:
            return True
        elif L[i] == L[j]:
            return _palin(L[(i+1):(-i-1)])
        else:
            return False
    return _palin(L)
#Sen pai way
#    x, y = n, 0
#    f = lambda: y * 10 + x % 10
#    while x > 0:
#        x, y = x // 10, f()
#    return y == n
    
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)
                 
def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def _print(i):
        print(i)
        if i == n - 1:
            print(n)
        else:
            _print(i + 1)
    _print(1)

# Better way    
def count_up_2(n):
    def counter(i):
        if i <= n:
            print(i)
            counter(i + 1)
    counter(1)    
