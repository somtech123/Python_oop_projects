import uuid

class Transaction:
    def __init__(self, amount: float, method: str):
        self.id = str(uuid.uuid4())[:8]
        self.amount = amount
        self.method = method
        self.status = 'PENDING'

    def __str__(self):
        return f'<Transaction {self.id} | {self.amount} | {self.method} | {self.status}'
    
    def __repr__(self):
        return self.__str__()