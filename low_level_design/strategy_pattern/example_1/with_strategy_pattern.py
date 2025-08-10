from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass

class CODPaymentStrategy(PaymentStrategy):
    def pay(self):
        print("Pay with COD is Successful")

class BkashPaymentStrategy(PaymentStrategy):
    def pay(self):
        print("Pay with Bkash is successful")

class NagadPaymentStrategy(PaymentStrategy):
    def pay(self):
        print("Pay with Nagad is successful")

class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self):
        print("Pay with Card is successful")

class PaymentMethods:
    def __init__(self):
        self.payment_strategy = None

    def set_strategy(self, strategy):
        self.payment_strategy = strategy

    def execute_strategy(self):
        if self.payment_strategy:
            self.payment_strategy.pay()
        else:
            print("No Payment Strategy Set.")


class CheckoutSystem:
    def main(self):
        payment_methods = PaymentMethods()
        order_amount = 500
        selected_method = "COD"

        if selected_method == "Bkash":
            payment_methods.set_strategy(BkashPaymentStrategy())
            payment_methods.execute_strategy()
        elif selected_method == "Nagad":
            payment_methods.set_strategy(NagadPaymentStrategy())
            payment_methods.execute_strategy()
        elif selected_method == "Card":
            payment_methods.set_strategy(CreditCardPaymentStrategy())
            payment_methods.execute_strategy()
        elif order_amount >= 500 and selected_method == "COD":
            payment_methods.set_strategy(CODPaymentStrategy())
            payment_methods.execute_strategy()
        else:
            print("Sorry! Minimum 500tk order is required for COD")


if __name__ == '__main__':
    CheckoutSystem().main()

