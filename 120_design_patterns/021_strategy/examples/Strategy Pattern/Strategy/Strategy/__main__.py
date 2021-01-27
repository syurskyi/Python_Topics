from strategies.strategy import Order, ShippingCost
from strategies.strategy import FedExStrategy, PostalStrategy, UPSStrategy

# Test Federal Express shipping

order = Order()
strategy = FedExStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
a__ cost == 3.0

# Test UPS shipping

order = Order()
strategy = UPSStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
a__ cost == 4.0

# Test Postal Service shipping

order = Order()
strategy = PostalStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
a__ cost == 5.0

print('Tests passed')
