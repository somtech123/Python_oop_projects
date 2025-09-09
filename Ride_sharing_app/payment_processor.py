from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amout: float) ->str:
        pass



class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, amout):
        return f'Paypal: Payment of {amout} processed. '
    
class StripePaymentProcessor(PaymentProcessor):
    def pay(self, amout):
        return f'Stripe: Payment of {amout} processed. '
    
class CryptoPaymentProcessor(PaymentProcessor):
    def pay(self, amout):
        return f'Crypto: Payment of {amout} processed in BTC.'