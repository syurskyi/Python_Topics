# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class SavinAccount(object):
    """Abstract class
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def withdrawal(self, ammount): raise NotImplementedError
    
class RegularSavingAccount(SavinAccount):

    def withdrawal(self, ammount):
        return ammount

class SalarySavingAccount(SavinAccount):

    def withdrawal(self, ammount):
        return ammount

class FixDepositeSavingAccount(SavinAccount):
    def withdrawal(self, ammount):
        return 'Not supported by this account type'

class AccountManager(object):
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
