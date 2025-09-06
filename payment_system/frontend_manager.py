from payment_method import paypal_payment_processor, crypto_payment_processor, stripe_payment_processor
from service import *

class FrontEndManager:

    def run(self):

        paypal_service = PaymentService(paypal_payment_processor.PayPalPaymentProcessor())

        crypto_service = PaymentService(crypto_payment_processor.CryptoPaymentProcessor())

        stripe_payment = PaymentService(stripe_payment_processor.StripePaymentProcessor())

        t1 = paypal_service.make_payment(150)
        t2 = stripe_payment.make_payment(100)
        t3 = crypto_service.make_payment(200)


        print(t1)
        print(t2)
        print(t3)

        paypal_service.refund_payment(t1)
        print(t1)

        print('All Transaction:', paypal_service.transaction + stripe_payment.transaction + crypto_service.transaction)

