# """
# "Metaclasses" section example of metaclass that reveal order of all its
# methods called.
# 
# """
# 
# print(" >>> defining RevealingMeta(type)")
# 
# 
# c_ RevealingMeta ty..
#     ___ -n mcs name bases namespace $$
#         print m.. "__new__ called")
#         r_ s___. -n ?  ?  ?  ?
# 
#     ??
#     ___ -p mcs name bases $$
#         print(m.. "__prepare__ called")
#         r_ s___ . -p n... b... $$
# 
#     ___ - cls name bases namespace $$
#         print c.. "__init__ called")
#         s___ . - n.. b.. n..
# 
#     ___ -c ___ $ $$
#         print ___ "__call__ called")
#         r_ s___ . -c $ $$
# 
# 
# print(" >>> defining RevealingClass(metaclass=RevealingMeta)")
# 
# 
# c_ RevealingClass m..
#     ___ -n cls
#         print(? "__new__ called")
#         r_ s___ . -n ?
# 
#     ___ -
#         print ? "__init__ called")
#         s___ . -
# 
# 
# __ _______ __ _______
#     print(" >>> Creating RevealingClass()")
#     instance _ R..
