# ### file: employees.py
#
#
# c_ Employee
#
#     ___ - ____, name, salary_0
#         ____.?  ?
#         ____.?  ?
#
#     ___ giveRaise ____ percent
#
#         ____.s.. _ ____.s.. + ____.s.. * p..
#
#     ___ work ____
#         print(____.n.., "does stuff")
#
#     ___ -r ____
#         return "<Employee: n.._@, s.._@>" / ____.? ____.?   # string
#
#
# c_ Chef ?
#
#     ___ - ____ name
#         E__.- ____ n.. 50000
#
#     ___ work ____
#         print(____.n.. "makes food")
#
#
# c_ Server E..
#
#     ___ - ____, name
#         E__.- ____ n.. 40000
#
#     ___ work ____
#         print(____.n... "interfaces with customer")
#
#
# c_ PizzaRobot C.
#
#     ___ - ____ name
#         C___.- ____ n...
#
#     ___ work ____
#         print(____.n.. "makes pizza")
#
# __ _____ __ _____
#     bob = P.R. bob       # Make a robot named bob
#     print('#' * 23 + ' Run inherited __repr__')
#     print(bob)                    # Run inherited __repr__
#     print('#' * 23 + ' Run type-specific action')
#     bob.work()                    # Run type-specific action
#     bob.giveRaise(0.20)           # Give bob a 20% raise
#     print('#' * 23 + ' Give bob a 20% raise')
#     print(bob); print()
#
#     print('#' * 23 + ' for klass in Employee, Chef, Server, PizzaRobot:')
#     ___ klass __ E... C... S... P..
#         obj _ ?|?. -n
#         ?.w..
#
