import uuid

class Payment:
    def __init__(self, ride_id: str, amount:float, processor):
        self.transaction_id = str(uuid.uuid4())[:8]
        self.ride_id = ride_id
        self.amount = amount
        self.processor = processor
        self.status = 'PENDING'

    def process_payment(self):
        result = self.processor.pay(self.amount)
        self.status = 'SUCCESS'
        return f'{result} (Transaction {self.transaction_id})'
    

    def __repr__(self):
        return f'<Payment {self.transaction_id} | Ride {self.ride_id} |{self.amount} |{self.status}'