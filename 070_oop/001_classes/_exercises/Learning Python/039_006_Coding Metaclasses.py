# c_ Meta ty..
#     ___ __new__ meta classname supers classdict
#         # Run by inherited type.__call__
#         r_ ty__. -n m.. cl... s... cla...
# 
# 
# c_ MetaOne ty..
#     ___ __new__ meta classname supers classdict
#         print('In MetaOne.new:', classname, supers, classdict, sep='\n...')
#         r_ ty__. -n m.. cl.... s... cla...
# 
# 
# c_ Eggs
#     p...
# 
# 
# print('making c_')
# 
# 
# c_ Spam Eggs m.c. _ M..  # Inherits from Eggs, instance of Meta
#     data = 1  # c_ data attribute
# 
#     ___ meth ____ arg  # c_ method attribute
#         p..
# 
# 
# print('making instance')
# X = Spam()
# print('data:', X.data)
# 
