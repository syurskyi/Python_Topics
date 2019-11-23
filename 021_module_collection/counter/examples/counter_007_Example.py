# Let's assume you are working for a company that produces different kinds of widgets.
# You are asked to identify the top 3 best selling widgets.
# You have two separate data sources - one data source can give you a history of all widget orders
# (widget name, quantity), while another data source can give you a history of widget refunds
# (widget name, quantity refunded).
# From these two data sources, you need to determine the top selling widgets (taking refinds into account of course).
# et's simulate both of these lists:
#
import random
from collections import defaultdict, Counter

random.seed(0)
widgets = ['battery', 'charger', 'cable', 'case', 'keyboard', 'mouse']
orders = [(random.choice(widgets), random.randint(1, 5)) for _ in range(100)]
refunds = [(random.choice(widgets), random.randint(1, 3)) for _ in range(20)]

print(orders)
print(refunds)

# Let's first load these up into counter objects.
# To do this we're going to iterate through the various lists and update our counters:

sold_counter = Counter()
refund_counter = Counter()

for order in orders:
    sold_counter[order[0]] += order[1]


for refund in refunds:
    refund_counter[refund[0]] += refund[1]

print(sold_counter)
# Counter({'case': 41,
#          'battery': 61,
#          'keyboard': 65,
#          'cable': 39,
#          'mouse': 46,
#          'charger': 35})

print(refund_counter)
# Counter({'battery': 7,
#          'charger': 5,
#          'cable': 9,
#          'keyboard': 7,
#          'mouse': 7,
#          'case': 5})

net_counter = sold_counter - refund_counter

net_counter

Counter({'case': 36,
         'battery': 54,
         'keyboard': 58,
         'cable': 30,
         'mouse': 39,
         'charger': 30})

net_counter.most_common(3)
# [('keyboard', 58), ('battery', 54), ('mouse', 39)]

# We could actually do this a little differently, not using loops to populate our initial counters.
# Recall the repeat() function in itertools:

from itertools import repeat

list(repeat('battery', 5))
# ['battery', 'battery', 'battery', 'battery', 'battery']

orders[0]
# ('case', 4)

list(repeat(*orders[0]))
# ['case', 'case', 'case', 'case']

# So we could use the repeat() method to essentially repeat each widget for each item of orders.
# We need to chain this up for each element of orders - this will give us a single iterable that we can then use
# in the constructor for a Counter object. We can do this using a generator expression for example:

from itertools import chain
print(list(chain.from_iterable(repeat(*order) for order in orders)))

order_counter = Counter(chain.from_iterable(repeat(*order) for order in orders))

print(order_counter)

# Counter({'case': 41,
#          'battery': 61,
#          'keyboard': 65,
#          'cable': 39,
#          'mouse': 46,
#          'charger': 35})

#### Alternate Solution not using Counter
# What if we don't want to use a Counter object. We can still do it (relatively easily) as follows:

net_sales = {}
for order in orders:
    key = order[0]
    cnt = order[1]
    net_sales[key] = net_sales.get(key, 0) + cnt

for refund in refunds:
    key = refund[0]
    cnt = refund[1]
    net_sales[key] = net_sales.get(key, 0) - cnt

# eliminate non-positive values (to mimic what - does for Counters)
net_sales = {k: v for k, v in net_sales.items() if v > 0}

# we now have to sort the dictionary
# this means sorting the keys based on the values
sorted_net_sales = sorted(net_sales.items(), key=lambda t: t[1], reverse=True)

# Top three
sorted_net_sales[:3]

# [('keyboard', 58), ('battery', 54), ('mouse', 39)]