# Payment System Project

The Payment System Project is a simple Python-based project that showcases the use of object-oriented programming (OOP) principles. It includes eight main classes: `PaymentProcessor`, `CryptoPaymentProcessor`, `PayPalPaymentProcessor`, `StripePaymentProcessor`, `PaymentService`, `Transaction`, `LoggerMixin` and `FrontendManager`. This project support multiple payment methods Paypal, Stripe, Crypto. it generate a new id for each transaction, keep a record of all transactions, allow refuns, log every payment(success/failure).


## Table of Contents

- [Introduction](#introduction)
- [Classes](#classes)
  - [PaymentProcessor](#employee)
  - [CryptoPaymentProcessor](#CryptoPaymentProcessor)
  - [PayPalPaymentProcessor](#PayPalPaymentProcessor)
  - [StripePaymentProcessor](#StripePaymentProcessor)
  - [Transaction](#Transaction)
  - [PaymentService](#PaymentService)
  - [Logger](#Logger)
  - [FrontEndManager](#FrontEndManager)

## Introduction

The Payment System Project demonstrates the implementation of object-oriented programming concepts in Python. It encompasses eight primary classes, each serving a distinct purpose:

### PaymentProcessor

The `PaymentProcessor` class represents an abstract class that define a common interface for all payment.


 ```
 pay(amount) with a return type of str
 refund(transaction_id) with a return type of str
```

### CryptoPaymentProcessor

The `CryptoPaymentProcessor` class is responsible implementing the concrete abstract method from the `PaymentProcessor` for crypto payment.

### PayPalPaymentProcessor

The `PayPalPaymentProcessor` class is responsible implementing the concrete abstract method from the `PaymentProcessor` for paypal payment.


### StripePaymentProcessor

The `StripePaymentProcessor` class is responsible implementing the concrete abstract method from the `PaymentProcessor` for stripe payment.

### Transaction

The `Transaction` Class represent a transaction class with these attributes
- `id`: The transaction id which is a unique id created with uuid module
- `amount`: The amount for that particular transaction
- `method`: The payment method used on the transaction
- `status`: The transaction status which is by default PENDING

### PaymentService

The `PaymentService` Class uses a `PaymentProcessor` (Composition) it handles creating transactions, logging and refund

### Logger(Mixin)

Resusable logging functionality


### FrontEndManager

The `FrontEndManager` class provides a user interface for interacting with the `PaymentService`. Users can perform actions such as:

- Make payments
- Make refunds on payment
