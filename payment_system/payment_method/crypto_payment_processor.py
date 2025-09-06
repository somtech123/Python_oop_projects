from payment_processor import *

class CryptoPaymentProcessor(PaymentProcessor):
    def pay(self, amout):
        return f'Crypto: Payment of {amout} processed in BTC.'
    
    def refund(seelf, transaction_id):
        return f'Crypto: Refund issued for transaction {transaction_id}. '