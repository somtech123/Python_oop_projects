from account import Account
from utility import CompoundInterestCalculator

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__( balance)
        self.__interest_rate = interest_rate

    def savings_interest_earned(self, monthly_deposit: float = 0, time = 1):
        
        interest = CompoundInterestCalculator.interest_earned(self._balance, monthly_deposit, self.__interest_rate, time)

        status = f'Interest Earned in {time} Year, is {interest:,.2f}' if monthly_deposit == 0 else f'Interest Earned in {time} Year, with monthly deposit of {monthly_deposit:,.2f} is {interest:,.2f}'

        self.log(status,'SavingsAccount',)

    
    def future_value_principal(self, monthly_deposit: float = 0, time = 1):
        fvp = CompoundInterestCalculator.futureValue(self._balance, monthly_deposit, self.__interest_rate, time)

        status = f'Future Principle on {self._balance:,.2f} in {time} Year, is {fvp:,.2f}' if monthly_deposit == 0 else f'Future Principle on {self._balance:,.2f} in {time} Year, with monthly deposit of {monthly_deposit:,.2f} is {fvp:,.2f}'

        self.log( status,'SavingsAccount',)
