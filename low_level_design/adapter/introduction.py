"""
Link(bangla) : https://hasanalihaolader.medium.com/অ্যাডাপ্টার-adapter-ডিজাইন-প্যাটার্ন-e8b897d0c2c0/
Link : https://algomaster.io/learn/lld/adapter
"""

"""
Incompatible legacy interface or class কে compatible করা হয় Adapter Pattern এর মাধ্যমে. 
Example হলো নিচের Bkash class যা Gateway Interface এর সাথে incompatible, যাকে compatible করা হয়েছে BkashAdapter class দ্বারা.
"""

# Payment GateWay
from abc import ABC, abstractmethod

class GateWay(ABC):
    @abstractmethod
    def get_amount(self):
        pass

    @abstractmethod
    def get_gateway_charge(self):
        pass


class SSLCommerz(GateWay):
    def __init__(self, amount, gateway_charge):
        self._amout = amount
        self._gateway_charge = gateway_charge

    def get_amount(self):
        return self._amout

    def get_gateway_charge(self):
        return self._gateway_charge


class GatewayHandler:
    def __init__(self, gateway: GateWay):
        self.gateway = gateway

    def calculate_price(self):
        amount = self.gateway.get_amount()
        charge = self.gateway.get_gateway_charge()

        print("Amount : ", amount)
        print("Charge : ", charge)
        print("Total Payable : ", (amount + charge))

# incompatible class (does NOT follow Gateway interface)
class Bkash:
    def __init__(self, amount, charging_percentage):
        self._amount = amount
        self._charging_percentage = charging_percentage

    def get_amount(self):
        return self._amount

    def get_charging_percentage(self):
        return self._charging_percentage

# Adapter Class to make Bkash compatible with Gateway interface
class BkashAdapter(GateWay):
    def __init__(self, bkash: Bkash):
        self._bkash = bkash

    def get_amount(self):
        return self._bkash.get_amount()

    def get_gateway_charge(self):
        # percentage simple calculation
        return (self._bkash.get_amount() * self._bkash.get_charging_percentage()) / 100.00


ssl_obj = SSLCommerz(1000, 8)
gateway_handler = GatewayHandler(ssl_obj)
gateway_handler.calculate_price()

# Bkash
bkash_obj = Bkash(1000, 1.85)
bkash_adapter = BkashAdapter(bkash_obj)
gateway_handler = GatewayHandler(bkash_adapter)
gateway_handler.calculate_price()
