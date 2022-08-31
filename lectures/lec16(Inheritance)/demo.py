class Account:
    """ An Account has a balance and holder

    >>> a = Account('John')
    >>> a.hodler
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    """
    # A class attribute
    interest = 0.02

    def __init__(self, account_hodler):
        """ Constrctor for class Accout """
        self.hodler = account_hodler # an instance attribute
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance -= amount
            return self.balance


#a = Account('John')
#a.deposit(100)
#print(a.interest)
#a.interest = 0.08
#print(a.interest)
#print(Account.interest)
#Account.interest = 0.09
#print(Account.interest)
#Account.test = 'lalala'

#Account.info = lambda self: self.hodler + " " +str(self.balance)
#print(a.info())


class CheckAccount(Account):
    """ A bank account that charges for deposit
    
    >>> ch = CheckAccount('Tom')
    >>> ch.interest
    0.01
    >>> ch.deposit(20)
    20
    >>> ch.withdraw(5)
    14
    """
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        return super().withdraw(amount + self.withdraw_fee)
        # return Account.withdraw(self, amount + self.withdraw_fee)