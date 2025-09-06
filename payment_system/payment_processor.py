from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amout: float) ->str:
        pass

    @abstractmethod
    def refund(seelf, transaction_id: str) -> str:
        pass