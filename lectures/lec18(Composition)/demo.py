########## Linked List Class ############
class Link:
    """ A Link list

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3, 4, 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> print(s)
    <3, 7, 5>
    >>> s.rest.rest = Link.empty
    >>> s
    Link(3, Link(7))
    >>> s.first = 6
    >>> print(s)
    <6, 7>
    >>> l = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> l
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(l)
    <1, <2, 3>, 4>
    """

    # empty end
    empty = ()
    
    # construt function
    def __init__(self, first, rest = empty):
        # check argument
        assert rest is Link.empty or isinstance(rest, Link)
        # assign
        self.first = first
        self.rest = rest

    def __repr__(self):
        # recursion call
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        # base case
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        # iterator of a list
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'


square, odd = lambda x: x * x, lambda x: x % 2 == 1


# Linked List Processing 
def range_link(start, end):
    """ Return a Linked List containing cosecutive ineger from start to end
    
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    # base case 
    if start == end:
        return Link.empty
    # recursion call
    return Link(start, range_link(start + 1, end))


def map_link(f, link):
    """ Return a Linked list that contains f(x) for each x in link

    >>> map_link(square, range_link(1, 5))
    Link(1, Link(4, Link(9, Link(16))))
    """
    # base case
    if link is Link.empty:
        return Link.empty
    # recursion call
    return Link(f(link.first), map_link(f, link.rest))


def filter_link(f, link):
    """ Return a Linked list that contains only element s x in link
    
    >>> filter_link(odd, range_link(1, 6))
    Link(1, Link(3, Link(5)))
    >>> map_link(square, filter_link(odd, range_link(1, 6)))
    Link(1, Link(9, Link(25)))
    """
    # base case
    if link is Link.empty:
        return Link.empty
    # recursion call
    if f(link.first):
        return Link(link.first, filter_link(f, link.rest))
    else:
        return filter_link(f, link.rest)


# Linked List Mutation
def add(link, v):
    """ Add v to link, return modified s

    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    assert link is not Link.empty
    if v < link.first:
        link.rest = Link(link.first, link.rest)
        link.first = v
    elif v > link.first:
        link.rest = add(link.rest, v)  if link.rest is not Link.empty else Link(v)
    return link


#####################################################################


########## Tree Class ##########
class Tree:
    """ A Tree is a label and a list of branches
    
    >>> t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    >>> t
    Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    >>> print(t)
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    def __init__(self, label, branches = []):
        self.label = label
        for b in branches:
            assert isinstance(b, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_repr = ', ' + repr(self.branches)
        else:
            branch_repr = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_repr) 

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return self.branches == []


def fib_tree(n):
    """ A Fibonacci tree

    >>> print(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    # base case 
    if n == 0 or n == 1:
        return Tree(n)
    left = fib_tree(n - 2)
    right = fib_tree(n - 1)
    fib_n = left.label + right.label
    return Tree(fib_n, [left, right])


def prune(t, n):
    """ Prune sub-trees whose lable value is n
    
    >>> t1 = fib_tree(4)
    >>> prune(t1, 1)
    >>> print(t1)
    3
      2
    >>> t2 = fib_tree(5)
    >>> prune(t2, 1)
    >>> print(t2)
    5
      2
      3
        2
    """
    assert n != t.label
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)


def leaves(tree):
    """ Return all leaves 

    >>> leaves(fib_tree(4))
    [0, 1, 1, 0, 1]
    """
    if tree.is_leaf():
        return [tree.label]
    return sum([leaves(b) for b in tree.branches], [])


def height(tree):
    """ Return height of tree

    >>> height(fib_tree(4))
    3
    """
    if tree.is_leaf():
        return 0
    return 1 + max([height(b) for b in tree.branches])