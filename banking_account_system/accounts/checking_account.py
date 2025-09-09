from account import Account
from utility import  *
from transaction import Transaction
from datetime import datetime

class CheckingAccount(Account):

    def __init__(self, balance, multiplier):
        super().__init__(balance)
        self.__multiplier = multiplier
        self.__creditworthiness_balance = 200
        self._is_creditworthy = False
        self.__debt = 0

    def __check_credit_worthiness(self):
        if self.__creditworthiness_balance >= 100 :
            self._is_creditworthy = True
        return self._is_creditworthy
    

    def over_draft_limit(self,wildCard: bool = False):
        if not self.__check_credit_worthiness():
            self.log('Sorry, you are not creditworthy at this time. Please withdraw an amount less than or equal to your balance.', 'CheckingAccount')
            return 0
        overdraft = self.__creditworthiness_balance * self.__multiplier
        self.log(f'You are egligibe to spend up to {overdraft:,.2f} from your overdraft') if wildCard == False else None
        return overdraft
    

    def withdraw(self, amount):
        is_credit_worthy = self.__check_credit_worthiness()

        # Check if current debt exceeds overdraft limit - deny if so
        # if self.__debt >= self.over_draft_limit(wildCard=True) or self.__debt < 0:
        if self.__debt < 0:
            self.log(f"Withdrawal denied: Your existing debt ({self.__debt:,.2f}) has reached or exceeded your overdraft limit ({self.over_draft_limit(wildCard=True):,.2f}). Please repay before withdrawing more.", 'CheckingAccount')
            self._balance = self.__debt
            return
        if amount <= self._balance:
            super().withdraw(amount)
        elif is_credit_worthy:
            available = self._balance + self.over_draft_limit(wildCard=True)
            if amount <= available: 
                self._balance -= amount
                limit = available - abs(self._balance)
                print(f"Withdrawal successful. OverDraft used {abs(self._balance):,.2f}. Available overdraft limit {limit:,.2f}")
                self.transaction.append(Transaction('Overdraft Withdrawal', self._balance, limit, datetime.now() ))
                self.__overDrawnBalance(abs(self._balance), 0.50, 10, 30)
            else:
              self.log(f"Transaction failed: Your overdraft limit is {self.over_draft_limit(wildCard=True):,.2f}, You cannot withdraw more than your balance + overdrawt limit.",'CheckingAccount')
        else:  self.log("Withdrawal denied: Insufficient funds and you are not credit worthy.",'CheckingAccount')

    
    def __overDrawnBalance(self, overDraft_used: float, dailyFees: float, annual_rate: float, days_overdrawn: int) ->float:
        total_payment = 0
        is_credit_worthy = self.__check_credit_worthiness()
        if not is_credit_worthy: total_payment = 0
        else:
         daily_rate = annual_rate / 365
         interest = overDraft_used * daily_rate * days_overdrawn
         total_fees = dailyFees * days_overdrawn
         total_payment = overDraft_used + interest + total_fees
         self.__debt = round(total_payment, 2)
         self.log(f'Your account is overdrawn by {round(total_payment, 2)}, Kindly repay back soon','CheckingAccount')
         return round(total_payment, 2)
        
    def repay_overDraft(self, amount):
        if self.__debt != 0:
            if amount >= abs(self.__debt):
                leftover = amount - abs(self._balance)
                self._balance = leftover
                self.__debt = 0
                self.log(f'No outstanding debt. New balance is: {self._balance:,.2f}', 'CheckingAccount')
                self.transaction.append(Transaction('Overdraft Repayment',amount, self._balance, datetime.now()))
            else:
                leftover = amount - abs(self.__debt)
                self._balance = leftover
                self.__debt = leftover
                self.log(f'Payment of {amount:,.2f} received towards your outstanding debt. \n Updated balance is: {self._balance:,.2f}, Kindly keep up the good work','CheckingAccount')
                self.transaction.append(Transaction('Overdraft Repayment',amount, self._balance, datetime.now()))
                 
        else: 
            self.log(f'You have no outstanding debt. \n successfully made deposit of {amount:,.2f} into your account', 'CheckingAccount')
            super().deposit(amount)


            

    

    




    

        

            

        
            
            



