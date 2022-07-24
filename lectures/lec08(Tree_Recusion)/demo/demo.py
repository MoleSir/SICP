def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


##############################
def cascade(n):
    """ Print a cascade prefixes of N
    
    >>> cascade(1234)
    1234
    123
    12
    1
    12
    123
    1234
    >>> cascade(1)
    1
    >>> cascade(123)
    123
    12
    1
    12
    123
    """
    # Base case:
    if n < 10:
        print(n)
    else:
        print(n)
        # recursion
        cascade(n // 10)
        print(n)

def cascade2(n):
    """ Print a cascade prefixes of N
    
    >>> cascade2(1234)
    1234
    123
    12
    1
    12
    123
    1234
    >>> cascade2(1)
    1
    >>> cascade2(123)
    123
    12
    1
    12
    123
    """ 
    print(n)
    if n >= 10:
        cascade2(n // 10)
        print(n)

############################################
def inverse_cascade(n):
    """ Print an inverse cascade prefixes of n

    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    >>> inverse_cascade(123)
    1
    12
    123
    12
    1
    >>> inverse_cascade(1)
    1
    """
    # print grow n
    grow(n // 10)
    # print n
    print(n)
    # print shrink n
    shrink(n // 10)

# function abstraction
def grow(n):
    # base case
    if n == 0:
        return
    grow(n // 10)
    print(n)

def shrink(n):
    # base case
    if n == 0:
        return
    print(n)
    shrink(n // 10)


####################Tree Recursion ###################
def fib(n):
    """ return fib:
    1 1 2 3 5 8 13 21 34 ...

    >>> fib(1)
    1
    >>> fib(0)
    1
    >>> fib(5)
    8
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


######## Hanoi ##########
def print_move(orgin, destination):
    """ print instruction to move a disk"""
    print("Move the top disk from rod", orgin, "to rod", destination)


def move_stack(n, start, end):
    """ print the moves required to move N disks on the start pole to the end

    Args:
        n: number of disks
        start: a pole position, either 1, 2, or 3
        end: a pole position, either 1, 2 or 3   

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_satck(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2 
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Illegal Input"
    # base case
    if n == 1:
        print_move(start, end)
    else:
        bridge = 6 - start - end
        move_stack(n - 1, start, bridge)
        print_move(start, end)
        move_stack(n - 1, bridge, end)



#################################################
def count_partitions(n, m):
    """ count the partitions of N using parts up to (no more) size of n
    
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(2, 4)
    2
    >>> count_partitions(6, 3)
    7
    """
    # base case
    if n == 0:
        return 1
    if n < 0:
        return 0

    # recurive call
    with_at_least_one_m = count_partitions(n - m, m)
    without_m = count_partitions(n, m - 1)
    return with_at_least_one_m + without_m

