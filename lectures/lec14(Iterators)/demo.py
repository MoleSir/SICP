class Countdown:
    """ Count down to zero

    >>> list(Countdown(5))
    [5, 4, 3, 2, 1]
    >>> for x in Countdown(3):
    ...     print(x)
    3
    2
    1
    """
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        v = self.start
        while v > 0:
            yield v
            v -= 1
    

###############################
def countdown(n):
    while n > 0:
        yield n
        n -= 1

x = countdown(5)

next(x)
next(x)
next(x)
next(x)

def countdown1(n):
    """ Lazily return n ~ 1

    >>> list(countdown1(4))
    [4, 3, 2, 1]
    """
    if n == 1:
        yield 1
    else:
        yield n
        yield from countdown1(n - 1)
