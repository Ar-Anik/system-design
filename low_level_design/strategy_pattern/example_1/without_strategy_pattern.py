class PaymentMethods:
    def __init__(self):
        self.selected_payment_method = None

    def set_selected_payment_method(self, method):
        self.selected_payment_method = method

    def pay(self):
        if self.selected_payment_method == 'COD':
            self._pay_with_cod()
        elif self.selected_payment_method == "Bkash":
            self._pay_with_bkash()
        else:
            print("Invalid Payment Method Selected!")

    def _pay_with_cod(self):
        print("Pay with COD is Successfully")
    def _pay_with_card(self):
        print("Pay with card is successful")

class CheckoutSystem:
    def main(self):
        payment_method = PaymentMethods()
        order_amount = 500
        selected_method = "COD"

        if selected_method == "Bkash":
            payment_method.set_selected_payment_method(selected_method)
            payment_method.pay()
        elif order_amount >= 500 and selected_method == "COD":
            payment_method.set_selected_payment_method(selected_method)
            payment_method.pay()
        else:
            print("Sorry! Minimum 500tk order is required for COD")


if __name__ == "__main__":
    CheckoutSystem().main()
