######################## pair #######################

def pair(first, second):
    """ Return a pair """

    def pair_func(selector):
        if selector == 'first':
            return first
        if selector == 'second':
            return second
    return pair_func

def first(p):
    """ return first elemet of p

    >>> p = pair(12, 3)
    >>> first(p)
    12
    """
    return p('first')

def second(p):
    """ return second element of p

    >>> p = pair(13, 2333)
    >>> second(p)
    2333
    """
    return p('second')
