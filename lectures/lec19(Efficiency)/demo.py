# 改进递归版本的 fib 函数
def fib(n):
    """ Return the n fibonaci number

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def memo(f):
    """ Reconstruct a single argument function into a memoized version """
    cache = {}
    def memoized(n):
        if n not in cache.keys():
            cache[n] = f(n)
        return cache[n]
    return memoized

# use memo 
fib_memo = memo(fib)

fib_memo(5)
fib_memo(6)


# More Efficiently
def make_memo_fib():
    """ Return memo fib function

    >>> memo_fib = make_memo_fib()
    >>> memo_fib(0)
    0
    >>> memo_fib(1)
    1
    >>> memo_fib(2)
    1
    >>> memo_fib(3)
    2
    >>> memo_fib(4)
    3
    >>> memo_fib(5)
    5
    """
    cache = {0 : 0, 1 : 1}
    def memo_fib(n):
        if n in cache.keys():
            return cache[n]
        res = memo_fib(n - 2) + memo_fib(n - 1)
        cache[n] = res
        return res
    return memo_fib



######################### Exponentitaion ###########################
# Linear time
def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n - 1)

# Logarithmic time
def square(x):
    return x * x

def exp_fast(b, n):
    if n == 0:
        return 1
    else n % 2 == 0:
        return square(exp_fast(b, n // 2))
    else:
        return b * exp_fast(b, n - 1)

# Quadratic time
def overlap(a, b):
    count = 0
    for item in a:
        for other in b:
            if item == other:
                count += 1
    return count

# Exponential time: fib(n)

# Constant time (1 + n)  * n / 2
def seqSum(n):
    return (1 + n) * n / 2




