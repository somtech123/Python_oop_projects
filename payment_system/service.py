from logger import LoggerMixin
from payment_processor import PaymentProcessor
from transaction import Transaction

class PaymentService(LoggerMixin):
     def __init__(self, processor: PaymentProcessor):
          self.processor = processor
          self.transaction = []

     def make_payment(self, amount: float):
          transaction = Transaction(amount, self.processor.__class__.__name__)
          
          result = self.processor.pay(amount)

          transaction.status == 'SUCCESS'

          self.transaction.append(transaction)

          self.log(result)

          return transaction
     
     def refund_payment(self, transaction: Transaction):
          result = self.processor.refund(transaction)

          transaction.status = 'REFUNDED'
          
          self.log(result)

          return transaction