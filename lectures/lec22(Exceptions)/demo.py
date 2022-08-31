def err():
    1/0

# ZeroDivisionError
# err()

# Assert 
def assert_func():
    assert False

print(__debug__)

# Raise Statements
def raise_error():
    raise TypeError('a test type error')

# raise_error()

# Try Statements
# try:
#    <try suit>
# except <exception class> as <name>:
#    <exceot suit>
try:
    raise_error()
except TypeError as z:
    print(z)

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0

# more except
try:
    raise_error()
except ZeroDivisionError as e:
    pass
except (TypeError, SyntaxError) as z:
    print(type(z), ':', z)


def div(a, b):
    return  a / b

def div_safe(a, b):
    try:
        return div(a, b)
    except ZeroDivisionError as z:
        print(type(z), ':', z)

print(div_safe(1, 2))
print(div_safe(2, 0))

print('hello')

# reduce
def reduce(f, s, initial):
    """ Combine elements of a pairwise using f, starting with initial
    
    E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8)
    >>> from operator import mul
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [1, 2, 3, 4], 2)
    16777216
    """
    if not s:
        return initial
    return reduce(f, s[1:], f(initial, s[0])) 


def divide_all(n, ds):
    """ Divide n by every d in ds.

    >>> divide_all(1024, [2, 4, 8])
    16.0
    >>> divide_all(1024, [2, 4, 0, 8])
    inf
    """
    from operator import truediv
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

    


