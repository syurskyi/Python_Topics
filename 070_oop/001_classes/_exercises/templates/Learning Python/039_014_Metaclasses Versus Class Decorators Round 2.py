# # Extend with a decorator: same as providing __init__ in a metaclass
# 
# ___ eggsfunc obj
#     r_ ?.value * 4
# 
# ___ hamfunc obj value
#     r_ value + 'ham'
# 
# ___ Extender aClass
#     ?.e.. _ e...                  # Manages class, not instance
#     ?.h..  _ h...                   # Equiv to metaclass __init__
#     r_ ?
# 
# _E..
# c_ Client1                               # Client1 = Extender(Client1)
#     ___ - ____ value               # Rebound at end of class stmt
#         ____.v.. _ v..
#     ___ spam ____
#         r_ ____.v.. * 2
# 
# _E..
# c_ Client2:
#     value = 'ni?'
# 
# X = _1('Ni!')                           # X is a Client1 instance
# print(?.s..
# print(?.e..
# print(?.h..('bacon'))
# 
# Y = _2
# print(?.e..
# print(?.h..('bacon'))
# 
