from payment_processor import *

class StripePaymentProcessor(PaymentProcessor):
    def pay(self, amout):
        return f'Stripe: Payment of {amout} processed. '
    
    def refund(seelf, transaction_id):
        return f'Stripe: Refund issued for transaction {transaction_id}. '