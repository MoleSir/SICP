def sum_digits_itr(n):
    """ Calculate the summation of all digits in n

    >>> sum_digits_itr(2019)
    12
    >>> sum_digits_itr(2022)
    6
    """
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

# use recursion:
def sum_digits_itr_recursion(n):
    """ Calculate the summation of all digits in n

    >>> sum_digits_itr_recursion(2019)
    12
    >>> sum_digits_itr_recursion(2022)
    6
    >>> sum_digits_itr_recursion(2922)
    15
    """
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sum_digits_itr_recursion(n // 10)

def factor(n):
    """ return n * n - 1 * ... * 1

    >>> factor(3)
    6
    >>> factor(4)
    24
    """
    if n == 1:
        return 1
    else:
        return n * factor(n - 1)


def is_even(n):
    """ Retruns whether n is even interger

    >>> is_even(0)
    True
    >>> is_even(128)
    True
    >>> is_even(1)
    False
    """
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    """ Return whether n is odd

    >>> is_odd(0)
    False
    >>> is_odd(1)
    True
    >>> is_odd(5)
    True
    >>> is_odd(6)
    False
    """
    if n == 0:
        return False
    return is_even(n - 1)