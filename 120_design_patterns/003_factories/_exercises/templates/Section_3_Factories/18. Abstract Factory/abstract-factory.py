# ____ a.. ______ A..
# ____ e.. ______ E.. au..
#
#
# c_ HotDrink A..
#     ___ consume
#         p..
#
#
# c_ Tea H..
#     ___ consume
#         print('This tea is nice but I\'d prefer it with milk')
#
#
# c_ Coffee H..
#     ___ consume
#         print('This coffee is delicious')
#
#
# c_ HotDrinkFactory A..
#     ___ prepare  amount
#         p..
#
#
# c_ TeaFactory H..
#     ___ prepare  amount
#         print _*Put in tea bag, boil water, pour |? ml, enjoy!')
#         r_ T..
#
#
# c_ CoffeeFactory H..
#     ___ prepare  amount
#         print _*Grind some beans, boil water, pour |? ml, enjoy!')
#         r_ C..
#
#
# c_ HotDrinkMachine
#     c_ AvailableDrink E..  # violates OCP
#         COFFEE = a..
#         TEA = a..
#
#     factories =    # list
#     initialized = F..
#
#     ___ -
#         __ no. ?i..
#             ?i.. _ T..
#             ___ d in ?A..
#                 name = ?.n.. 0 + ?.n.. 1: .lo..
#                 factory_name = ? + 'Factory'
#                 factory_instance = ev..  ?
#                 ?f__.ap.. n.. ?
#
#
#
#
#
#     ___ make_drink
#         print('Available drinks:')
#         ___ f __ ?f..
#             print ? 0
#
#         s = i..  _*Please pick drink |0-|le. ?f..|-1||: '
#         idx = in. ?
#         s = i.. _*Specify amount: ')
#         amount = in. ?
#         r_ ?f.. |idx 1.pr.. am..
#
#
#
# ___ make_drink type
#     __ ? __ 't..
#         r_ T__.p..200
#     ____ ? __ 'c..
#         r_ C___.p.. 50
#     ____
#         r_ N..
#
#
# __ _______ __ _____
#     # entry = input('What kind of drink would you like?')
#     # drink = make_drink(entry)
#     # drink.consume()
#
#     hdm = H..
#     drink = ?.m..
#     ?.c..
