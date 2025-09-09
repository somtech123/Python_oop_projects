from accounts.checking_account import *
from accounts.fixed_deposit_account import *
from accounts.savings_account import *

class User:
    def __init__(self, userName, password, address,  checking_balance = 0.0, saving_balance= 0.0, fixed_account_balance=0.0, checking_multiplier=2, majority_year= 6, saving_interest_rate=2):
        self.userName = userName
        self.password = password
        self.address = address 
        self.checkingAccount = CheckingAccount(checking_balance, checking_multiplier)
        self.fixedAccount = FixedDeposit(fixed_account_balance, majority_year)
        self.savingAccount = SavingsAccount(saving_balance, saving_interest_rate)


    
    def __str__(self):
        return ';;;;'