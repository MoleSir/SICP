def fib(n):
    """ return fibonacii number
    Args:
        n >= 1
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    
    >>> fib(1)
    1
    >>> fib(3)
    2
    >>> fib(8)
    21
    >>> fib(9)
    34
    """
    if n <= 2:
        return 1
    f1, f2 = 1, 1
    i = n - 2
    result = 0
    while i > 0:
        result = f1 + f2
        f1 = f2
        f2 = result
        i = i - 1
    return result
        
################################################

def area_square(x):
    """ return square's area """
    return x * x

def area_circle(x):
    """ return circle's area """
    return 3.1415926 * x * x

def area_hexagon(x):
    """ return regular hexagon' area """
    return x * x * sqrt(3) / 2


# after generalization with arguments

def area(r, shape_const):
    """ return the area of a shape """
    assert r > 0
    return r * r * shape_const

def square(r):
    return area(r, 1)

def circle(r):
    return area(r, 3.1415926)

def hexagon(r):
    return area(r, sqrt(3) / 2)



############################################

def sum_natural(n):
    """ sum the n natural numbers 

    >>> sum_natural(5)
    15
    """
    if n <= 0:
        return 0
    sum, i = 0, 1
    while i <= n:
        sum += i
        i += 1
    return sum

def sum_cubes(n):
    """ sum of cubes number 

    >>> sum_cubes(5)
    225
    """
    if n <= 0:
        return 0
    sum, i = 0, 1
    while i <= n:
        sum += i * i * i
        i += 1
    return sum


# after generalization with arguments
def natural(i):
    return i
def cube(i):
    return i * i * i
def split_term(i):
    return 8 / ((4 * i - 3) * (4 * i - 1))

def sum(n, func):
    """ sum of n's func sequence number 

    >>> sum(5, cube)
    225
    >>> sum(5, split_term)
    3.041839618929402
    """
    if n <= 0:
        return 0
    sum, i = 0, 1
    while i <= n:
        sum += func(i)
        i += 1
    return sum


###############################
    
def make_adder(n):
    """ return a function: adder

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    >>> make_adder(4)(9)
    13
    """
    def adder(k):
        return n + k
    return adder


##############################

# lambda: only a return, no statements
func = lambda a, b: a + b
print(func(1, 2))


###############################

def condition():
    print("This is a condition.")
    return True
def if_suite():
    print("This is a suite.")
def else_suite():
    print('This is elase suite.')

def if_(conditional_value, if_value, else_value):
    if conditional_value:
        return if_value
    else:
        return else_value

def if_statement():
    if condition():
        if_suite()
    else:
        else_suite()

def if_function():
    if_(condition(), if_suite(), else_suite())
