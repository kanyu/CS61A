def mul(a, b):
    return a * b
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]
print(divisors(4))

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

reduce(mul, [2, 4, 8], 1)


def group_by_key(pairs):
    """
    >>> example = [[1,2], [3,2], [1,3], [3,1], [1,2]]
    >>>group_by_key(example)
    {1: [2,3,2], 3:[2,1]}
    """
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = [value]
        else:
            d[key].append(value)
    # return d
print()
