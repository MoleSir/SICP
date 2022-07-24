###################### rational #####################
# Rational Arithmetic
def add_rational(x, y):
    """ return the sum of x and y
    which is also a rational

    >>> x = rational(3, 2)
    >>> y = rational(4, 3)
    >>> z = add_rational(x, y)
    >>> numer(z)
    17
    >>> denom(z)
    6
    """
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    """ return the mul of x and y
    which is also a rational

    >>> x = rational(3, 2)
    >>> y = rational(4, 3)
    >>> z = mul_rational(x, y)
    >>> numer(z)
    2
    >>> denom(z)
    1
    """    
    return rational(numer(x) * numer(y),
                    denom(x) * denom(y))


def equal_rational(x, y):
    """ return whether  x equal y
    which is also a rational

    >>> x = rational(3, 2)
    >>> y = rational(6, 4)
    >>> z = rational(2, 3)
    >>> equal_rational(x, y)
    True
    >>> equal_rational(y, z)
    False
    """ 
    return numer(x) * denom(y) ==  numer(y) * denom(x)


def print_rational(x):
    """ Print rational x

    >>> x = rational(2, 3)
    >>> print_rational(x)
    2 / 3
    """ 
    print(numer(x), '/', denom(x))



# Construter and Selectors
from math import gcd

def rational(n, d):
    """ Return a representation of the rational number N / D
    """
    g = gcd(n, d)
    n, d = n // g, d // g
    return [n, d]

def numer(x):
    """ return the numerator of rational x
    
    >>> x = rational(3, 2)
    >>> numer(x)
    3
    """
    return x[0]

def denom(x):
    """ return thr demoinator of rational number x

    >>> x = rational(3, 2)
    >>> denom(x)
    2
    """
    return x[1]




