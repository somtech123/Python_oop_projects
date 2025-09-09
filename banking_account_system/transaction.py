from datetime import datetime
class Transaction:
    def __init__(self,operation: str, amount: float, balance: float, date: datetime):
        self.operation = operation
        self.amount = amount
        self.balance = balance
        self.dateTime = date


    def __repr__(self):
        return f'Transaction: description = {self.operation} | amount = {self.amount:,.2f} | current balance = {self.balance:,.2f}, time: {self.dateTime.strftime('%Y-%m-%d %H:%M:%S')} \n'