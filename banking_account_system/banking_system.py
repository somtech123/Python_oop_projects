from account import Account
from user import User
from logger import LoggerMixin

class BankingServices(LoggerMixin):
    def __init__(self):
        self.user = {}

    def create_user(self, username:str, password:str,address:str, checking_balance = 0.0, saving_balance= 0.0, fixed_account_balance=0.0, checking_multiplier=2, majority_year= 6,saving_interest_rate=2,):
        if username in self.user:
            self.log('Username already exits')
        else:
            self.user[username] = User(username, password, address, checking_balance, saving_balance, fixed_account_balance, checking_multiplier,majority_year, saving_interest_rate)
            self.log('Username created successfully')

    
    def login_user(self, username:str, password:str) -> User:
       user = self.user.get(username)
       if user and user.password == password:
           self.log('Login successfully')
           return user
       else:
           self.log('wrong credential')
           return None
       