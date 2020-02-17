# ______ six
# ____ a... _______ A..
# 
# 
# ?six.add_metaclass A..
# c_ Abstract_Coffee o..
# 
#     ___ get_cost 
#         p..
# 
#     ___ get_ingredients
#         p...
# 
#     ___ get_tax 
#         r_ 0.1 * ?g_c..
# 
# 
# c_ Concrete_Coffee A..
# 
#     ___ get_cost 
#         r_ 1.00
# 
#     ___ get_ingredients 
#         r_ 'coffee'
# 
# 
# ?six.add_metaclass A..
# c_ Abstract_Coffee_Decorator A..
# 
#     ___ - decorated_coffee
#         ?  ?
# 
#     ___ get_cost
#         r_ ?d___.g...
# 
#     ___ get_ingredients 
#         r_ ?d___.g_i..
# 
# 
# c_ Sugar A_C_D...
# 
#     ___ - decorated_coffee
#         A__. - ?
# 
#     ___ get_cost 
#         r_ ?d___.g..
# 
#     ___ get_ingredients 
#         r_ ?d__.g_i.. + ', sugar'
# 
# 
# c_ Milk A_C_D..
# 
#     ___ - d..
#         A___. - ?
# 
#     ___ get_cost 
#         r_ ?d__.g_c.. + 0.25
# 
#     ___ get_ingredients
#         r_ ?d___.g_i.. + ', milk'
# 
# 
# c_ Vanilla A_C__D..
# 
#     ___ - decorated_coffee
#         A___. - ?
# 
#     ___ get_cost 
#         r_ ?d__.g_c.. + 0.75
# 
#     ___ get_ingredients
#         r_ ?d__.g_i.. + ', vanilla'
