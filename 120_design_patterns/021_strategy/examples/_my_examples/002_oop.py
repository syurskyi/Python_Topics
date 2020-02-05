from abc import ABCMeta, abstractmethod

class AbsStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        print("This is abstract method")


class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        print("This is used FedExStrategy and cost 3$")
        # return 3.00


class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        print("This is used PostalStrategy and cost 5$")
        return 5.00


class UPSStrategy(AbsStrategy):
    def calculate(self, order):
        print("This is used UPSStrategy and cost 4$")
        return 4.00


class Order(object):
    def __init__(self):
        print('This is order')


class ShippingCost(object):
    def __init__(self, strategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate(order)


# Fed shipping
order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)

print()
# UPS shipping
order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)

print()
# Postal Service shipping
order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)