from abc import ABCMeta, abstractmethod


class AbsStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        """ Calculate shipping cost"""

class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3.00

class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.00

class UPSStrategy(AbsStrategy):
    def calculate(self, order):
        return 4.00

class Order(object):
    def __init__(self):
        pass


class ShippingCost(object):
    def __init__(self, strategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate(order)

order = Order()
strategy = FedExStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
cost == 3.0
# assert cost == 3.0

# Test UPS shipping

order = Order()
strategy = UPSStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
# assert cost == 4.0

# Test Postal Service shipping

order = Order()
strategy = PostalStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
# assert cost == 5.0

# print('Tests passed')