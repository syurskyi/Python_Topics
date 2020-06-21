# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# Base Interface's
class SavinAccount(object):
    """Abstract class
    """
    __metaclass__ = ABCMeta

class SavinAccountWithWithdrawal(SavinAccount):
    """Abstract class
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def withdrawal(self, ammount): raise NotImplementedError
    
class SavinAccountWithoutWithdrawal(SavinAccount):
    """Abstract class
    """
    __metaclass__ = ABCMeta


# Child Class

class RegularSavingAccount(SavinAccountWithWithdrawal):

    def withdrawal(self, ammount):
        return ammount

class SalarySavingAccount(SavinAccountWithWithdrawal):

    def withdrawal(self, ammount):
        return ammount

class FixDepositeSavingAccount(SavinAccountWithoutWithdrawal):
    def __init__(self):
        pass


# Decorator

def verifiy_withdrawal(func):
    def inner(*argv):
        if not issubclass(type(argv[1]), SavinAccountWithWithdrawal) : print("%s is a type %s, the function need a SavinAccountWithWithdrawal type" % (argv[1], type(argv[1]))); exit(0)
        return func(*argv)
    return inner

    
# Context Manager

class AccountManager(object):

    @verifiy_withdrawal
    def withdrawFromAccount(self, account, ammount):
        print(account.withdrawal(ammount))


if __name__ == '__main__':
    regular_saving_account = RegularSavingAccount()
    salary_saving_account = SalarySavingAccount()
    fix_deposite_saving_account = FixDepositeSavingAccount()
    ammount = 100
    
    account_manager = AccountManager()
    account_manager.withdrawFromAccount(regular_saving_account, ammount)
    account_manager.withdrawFromAccount(salary_saving_account, ammount)
    account_manager.withdrawFromAccount(fix_deposite_saving_account, ammount)


