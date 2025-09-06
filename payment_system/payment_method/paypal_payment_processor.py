from payment_processor import *

class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, amout):
        return f'Paypal: Payment of {amout} processed. '
    
    def refund(seelf, transaction_id):
        return f'Paypal: Refund issued for transaction {transaction_id}. '