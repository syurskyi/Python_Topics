# ____ a.. _______ A.. a..
#
#
# c_ PizzaFactory m..
#
#     ??
#     ___ createVegPizza
#         p..
#
#     ??
#     ___ createNonVegPizza
#         p..
#
# c_ IndianPizzaFactory P..
#
#     ___ createVegPizza
#         r_ D..
#     ___ createNonVegPizza
#         r_ C..
#
# c_ USPizzaFactory P..
#
#     ___ createVegPizza
#         r_ M..
#     ___ createNonVegPizza
#         r_ H..
#
# c_ VegPizza m..
#
#     ??
#     ___ prepare VegPizza
#         p..
#
# c_ NonVegPizza m..
#
#     ??
#     ___ serve VegPizza
#         p..
#
# c_ DeluxVeggiePizza V..
#
#     ___ prepare
#         print("Prepare ", ty.. ____. -n
#
# c_ ChickenPizza N..
#
#     ___ serve  VegPizza
#         print(ty.. ____. -n, " is served with Chicken on ", ty.. V... -n
#
# c_ MexicanVegPizza V..
#
#     ___ prepare
#         print("Prepare ", ty.. ____ . -n
#
# c_ HamPizza N..
#
#     ___ serve VegPizza)
#         print(ty.. _____. -n " is served with Ham on ", ty..  V.. -n
#
# c_ PizzaStore
#
#     ___ -
#         p..
#
#     ___ makePizzas
#         ___ factory __ I.., U..
#             ?factory = f..
#             ?N.. = ?f__.c..
#             ?V.. = ?f__.c..
#             ?V__.p..
#             ?N__.s.. ?V..
#
#
# pizza = PizzaStore()
# pizza.makePizzas()