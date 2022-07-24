#######################################
# [] is a list
a = []
a = [1, 2, 3]


def count_occurance(lst, ele):
    """ count the number of ele in lst
    """
    count = 0
    for e in lst:
        if e == ele:
            count += 1
    return count



#####################################
# range() 
def sum_itr(lst):
    """ return sum of lst """
    sum = 0
    for e in lst:
        sum += e
    return sum

def sum_rec(lst):
    # base case
    if len(lst) == 0:
        return 0
    return lst[0] + sum_rec(lst[1:])

def if_fun(n):
    if n:
        print("Yes")
    else:
        print("No")


##########################################
# <map exp> for <name> in <iter exp> if <filter exp>
def my_for_sugger(oper, lst, predi):
    res = []
    for e in lst:
        if predi(e) == True:
            res.append(oper(e))
    return res


#########################################
def reverse_string_itr(s):
    """ reverse a string s, and return

    >>> reverse_string_itr('123456')
    '654321'
    >>> reverse_string_itr('yechen')
    'nehcey'
    """
    res = ''
    for e in s:
        res = e + res
    return res


def reverse_string_rec(s):
    """ reverse a string s, and return

    >>> reverse_string_rec('123456')
    '654321'
    >>> reverse_string_rec('yechen')
    'nehcey'
    """
    # base case
    if len(s) == 1:
        return s
    else:
        return reverse_string_rec(s[1:]) + s[0]