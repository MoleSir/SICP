print('hello world')

# multiple return values
def multiple(a, b):
    return a, b

x, y = multiple(1, 3)
print(x, y)

# default argument
# default argument and right
def increase(n, k = 1):
    return n + k

n = 1
print(n)
n = increase(n)
print(n)
n = increase(n, 3)
print(n)


# compound statements
def add(a, b):
    return a + b

print(add(12,3.3))


def abs(x):
    if x < 0:
        return -1 * x
    elif x == 0:
        return 0
    else:
        return x

# while statemrnts
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i

# Prime Factorization
def Prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return i
        i = i + 1
    return num


def prime_factorization(n):
    """print

    Args:
        n (int): a postive integer
    >>> prime_factorization(-1)
    >>> prime_factorization(1)
    >>> prime_factorization(8)
    2
    2
    2
    >>> prime_factorization(9)
    3
    3
    >>> prime_factorization(858)
    2
    3
    11
    13
    """
    if n <= 1:
        return
    i = 2
    while n != 1:
        if n % i == 0:
            print(i)
            n = n // i
            i = 2
        else:
            i = i + 1