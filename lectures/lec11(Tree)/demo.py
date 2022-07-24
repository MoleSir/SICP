#################### tree ######################
def tree(label, branches = []):
    """ Construction of tree
    
    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> t
    [3, [1], [2, [1], [1]]]
    >>> label(t)
    3
    >>> branches(t)
    [[1], [2, [1], [1]]]
    >>> is_tree(t)
    True
    >>> is_leaf(t)
    False
    """
    # list is constrution of list, it will buil a new list, but copy
    for b in branches:
        assert is_tree(b)
    return [label] + list(branches)


def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for b in branches(t):
        if not is_tree(b):
            return False
    return True

def branches(t):
    """ Branch selector of tree """
    return t[1:]

def label(t):
    return t[0]

def is_leaf(t):
    return not branches(t)


######################################################
def count_leaves(t):
    """ Count leaves number of t

    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> count_leaves(t)
    3
    """
    # base case
    if is_leaf(t):
        return 1
    # recurion call
    return sum([count_leaves(b) for b in branches(t)])


def leaves(t):
    """ Return a list of all leaves in tree T

    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> leaves(t)
    [1, 1, 1]
    """
    # base case
    if is_leaf(t):
        return [label(t)]
    # recursion call
    return sum([leaves(b) for b in branches(t)], [])


def copy_tree(t):
    """ Return another tree which is the same as T but is not T

    >>> t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> t2 = copy_tree(t1)
    >>> t1 == t2
    True
    >>> t1 is t2
    False
    """
    # base case
    if is_leaf(t):
        return tree(label(t))
    # recurion call
    return tree(label(t), [copy_tree(b) for b in branches(t)])


def print_tree(t, indent = 0):
    """ Print a tree

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> print_tree(t)
    3
      1
      2
        1
        1
    >>> t = tree(3, [tree(1, [tree(4), tree(5)]), tree(2, [tree(1), tree(1)])])
    >>> print_tree(t)
    3 
      1
        4
        5
      2
        1
        1
    """
    # print root first
    print("  " * indent + str(label(t)))
    # loop for each branch
    for b in branches(t):
        # recursion call
        print_tree(b, indent + 1)


def sum_path(t):
    """ Return a list of all paths in T

    >>> t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> sum_path(t1)
    [[3, 1], [3, 2, 1], [3, 2, 1]]
    >>> t2 = tree(3, [tree(1, [tree(4), tree(5)]), tree(2, [tree(1), tree(1)])])
    >>> sum_path(t2)
    [[3, 1, 4], [3, 1, 5], [3, 2, 1], [3, 2, 1]]
    """
    # base case
    if is_leaf(t):
        return [[label(t)]]
    # recursion call
    res = []
    for b in branches(t):
        paths = sum_path(b)
        for p in paths:
            res.append([label(t)] + p)
    return res 
