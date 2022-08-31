# 对象有两种表示，一个便于人阅读，一个便于程序解析
# 在 python 中 repr 函数可以获取对象的便于程序解析的字符串表达式
# str 可以获取对象便于人类阅读的字符串表达式
# str 是一个 class

from fractions import Fraction
half = Fraction(1, 2)
print(repr(half))
print(str(half))
# print 函数打印的是 str 函数解析得到的字符串表达式
print(half)


#############################
print(half.__repr__())
print(half.__str__())


######### 自己实现 repr 与 str #############
# python 本身也是这样实现的，会先取出对象的类型，调用整个类型都一致
# 的 __repr__ 与 __str__，如果直接使用对象调用可能会调用到某个对象
# 特有的 instance attribute
def _repr(x):
    """
    Return the repr string od object x

    >>> from fractions import Fraction
    >>> half = Fraction(1, 2)
    >>> _repr(half) == repr(half)
    True
    """
    s = type(x).__repr__(x)
    if not isinstance(s, str):
        raise TypeError
    return s

def _str(x):
    s = type(x).__str__(x)
    if not isinstance(s, str):
        raise TypeError
    return s


########### special method names in python ##########
# Certain names are special because they have built-in behavior
# These names always start and end with two underscores
# __init__ Method invoked automatocally when an object is constructed
# __repr__ 
# __add__
# __bool__
# __float__


class Bear:
    """ A Bear
    
    >>> bearSir = Bear()
    >>> bearSir
    Bear()
    >>> print(bearSir)
    a bear
    >>> repr(bearSir)
    'Bear()'
    >>> str(bearSir)
    'a bear'
    >>> bearSir.__repr__()
    'instance bear repr'
    >>> bearSir.__str__()
    'instance bear str'
    >>> bool(bearSir)
    False
    >>> float(bearSir)
    1.1
    """

    def __init__(self):
        # instance attribute
        self.__repr__ = lambda: 'instance bear repr'
        self.__str__ = lambda: 'instance bear str'

    def __repr__(self) -> str:
        return 'Bear()'
    
    def __str__(self) -> str:
        return 'a bear'

    def __add__(self):
        pass

    def __bool__(self):
        return False

    def __float__(self):
        return 1.1



########### Ratio numbers ###########
from math import gcd

class Ratio:
    """  A mutable ratio

    >>> f = Ratio(9, 15)
    >>> f
    Ratio(9, 15)
    >>> print(f)
    9/15

    >>> Ratio(1, 3) + Ratio(1, 6)
    Ratio(1, 2)
    >>> Ratio(1, 3) + 1
    Ratio(4, 3)
    >>> 1 + f
    Ratio(8, 5)
    >>> 1.4 + f 
    2.0
    """

    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __float__(self):
        return self.numer / self.denom

    def __add__(self, other):
        if isinstance(other, Ratio):
            n = self.numer * other.denom + other.numer * self.denom
            d = self.denom * other.denom
        elif isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        else:
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    __radd__ = __add__










