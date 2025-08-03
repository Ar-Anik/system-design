from abc import ABC, abstractmethod

class PaymentStatusService(ABC):
    @abstractmethod
    def get_status(self, payment_id):
        pass

class CreditCardPaymentStatus(PaymentStatusService):
    def get_status(self, payment_id):
        return "success"

class PayPalStatus(PaymentStatusService):
    def get_status(self, payment_id):
        return {'status': "success"}

payment_status = CreditCardPaymentStatus()
print(payment_status.get_status(1008))

payment_status = PayPalStatus()
print(payment_status.get_status(1004))

"""
Here, LSP is violated: We can no longer rely on get_status() returning a consistent type. A caller expecting a str 
might break if a dict is returned.
"""

# Good Design (LSP-compliant)
class PaymentStatusService(ABC):
    @abstractmethod
    def get_status(self, payment_id) -> dict:
        pass

class CreditCardPaymentStatus(PaymentStatusService):
    def get_status(self, payment_id):
        return {"status": "success"}

class PayPalStatus(PaymentStatusService):
    def get_status(self, payment_id):
        return {"status": "success"}

def check_payment_status(service: PaymentStatusService, payment_id: int):
    result = service.get_status(payment_id)

    if result.get("status") == "success":
        print("Payment completed.")
    else:
        print("Payment failed.")

check_payment_status(CreditCardPaymentStatus(), 1008)
check_payment_status(PayPalStatus(), 1004)

"""
Now it's LSP-compliant: We can substitute CreditCardPaymentStatus or PayPalStatus for PaymentStatusService and everything works.
"""