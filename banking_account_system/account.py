from logger import LoggerMixin
from transaction import Transaction
from datetime import datetime


class Account(LoggerMixin):
    def __init__(self, balance: float):
      
        self._balance = balance
        self.transaction = []

    
    def deposit(self, amount: float):
        self._balance += amount
        self.transaction.append(Transaction('Deposit',amount, self._balance, datetime.now()))
        self.log(f'Your Deposit of {amount:,.2f} was successfuly made, available balance: {self._balance:,.2f}','Account')

   
    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
            self.transaction.append(Transaction('Withdrawal',amount, self._balance, datetime.now()))
            self.log(f'Your Withdrawal of {amount:,.2f} was successfuly made, available balance: {self._balance:,.2f}','Account')
        else: self.log(f'You have Insufficient funds, available balance: {self._balance:,.2f}','Account')

    
    def get_history(self):
        self.log([t for t in self.transaction], 'Account')
        return [t for t in self.transaction]

    # @abstractmethod
    # def transfer(self, amount: float, account) -> str:
    #     pass




    
