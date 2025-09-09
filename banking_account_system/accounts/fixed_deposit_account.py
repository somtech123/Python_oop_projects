from account import Account
from utility import *
from transaction import Transaction
from datetime import datetime

class FixedDeposit(Account):

    def __init__(self, balance, majority_year: int):
        super().__init__( balance)
        self.majority_year = majority_year
       

    def __years_held_interest(self, years_held: int, base_interest=2, increament=1, max_interest=8):
        """
        The interest rate starts at 2% before maturity.
        At maturity, it jumps by 3% (to 5%).
        After maturity, it increases by 1% each year.
        Interest can never go over 10%.
        """

        if years_held < self.majority_year:
            interest = base_interest
        elif years_held == self.majority_year:
            interest = base_interest + 3
        else:
            interest = base_interest + 3 + (years_held - self.majority_year) * increament
        return min(interest, max_interest)


    def withdraw(self, amount: float, years_held: int = None):
        if years_held is None:
            years_held = self.majority_year

        interest = self.__years_held_interest(years_held)
        match years_held:
            case t if t < self.majority_year:
                msg = 'Withdrawal before majurity: Your deposit has not yet completed the fixted term.'
           
            case t if t ==  self.majority_year:
                msg = 'Withdrawal at maturity: Your fixed deposit has reached it\'s full term.'
              
            case t if t >  self.majority_year:
                msg = 'Withdrawal after maturity: Incentive added for holding beyound fixed term'
            case _:
                self.log('Invalid request')
                return 
            
        fd_maturity = CompoundInterestCalculator.compound_value(self._balance, interest, years_held)
        self.log(f'Fixed deposit of: {self._balance:,.2f} held for {years_held} years on an interest of {interest}% is: {fd_maturity:,.2f}','FixedDeposit')
        if amount > fd_maturity:
            self.log('You have Insufficient funds, available balance:','FixedDeposit')
        else: 
            fd_maturity -= amount
            self._balance = fd_maturity
            self.transaction.append(Transaction('Fixed Deposit Withdrawal',amount, self._balance, datetime.now()))
            self.log(msg + f' Your new balance is: {self._balance:,.2f}','FixedDeposit')

    
    def check_interest_earn(self, years_held: int = None):
        if years_held is None:
            years_held = self.majority_year

        interest = self.__years_held_interest(years_held)
        fd_interest = CompoundInterestCalculator.coumpound_interest_earned(self._balance, interest,years_held)
        self.log(f'You have earned {fd_interest:,.2f} after {years_held} years','FixedDeposit')
        return round(fd_interest,2)
    
    # def get_history(self):
    #     lst = list().f




