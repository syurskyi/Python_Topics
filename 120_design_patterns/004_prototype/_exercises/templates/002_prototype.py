# ______ c__
# 
# 
# c_ Prototype:
#     _type _ N..
#     _value _ N..
# 
#     ___ clone
#         p..
# 
#     ___ getType
#         r_ _t..
# 
#     ___ getValue
#         r_ _v..
# 
# 
# c_ Type1 P..
# 
#     ___ - number
#         _t.. _ "Type1"
#         _v.. _ ?
# 
#     ___ clone
#         r_ c____.c___ ?
# 
# 
# c_ Type2 P..
#     """ Concrete prototype. """
# 
#     ___ - number
#         _t.. _ "Type2"
#         _v.. _ ?
# 
#     ___ clone
#         r_ c____.c___ ?
# 
# 
# c_ ObjectFactory
#     """ Manages prototypes.
#     Static factory, that encapsulates prototype
#     initialization and then allows instatiation
#     of the classes from these prototypes.
#     """
# 
#     __type1Value1 _ N..
#     __type1Value2 _ N..
#     __type2Value1 _ N..
#     __type2Value2 _ N..
# 
#     ??
#     ___ initialize
#         ?.__1 _ T1 1
#         ?.__2 _ T1 2
#         ?.__2_1 _ T2 1
#         ?.__2_2 _ T2 2
# 
#     ??
#     ___ getType1Value1
#         r_ ?.__1.cl..
# 
#     ??
#     ___ getType1Value2
#         r_ ?.__2.cl..
# 
#     ??
#     ___ getType2Value1
#         r_ ?.__2_1.cl..
# 
#     ??
#     ___ getType2Value2():
#         r_ ?.__2_2.clone()
# 
# 
# ___ main
#     ?.i...
# 
#     instance _ ?.ge_1
#     print("@: @"  ?.gT.. ?.gV..
# 
#     instance _ ?.ge_2
#     print("@: @"  ?.gT.. ?.gV..
# 
#     instance _ ?.ge_2__1
#     print("@: @"  ?.gT.. ?.gV..
# 
#     instance _ ?.ge_2_2
#     print("@: @"  ?.gT.., ?.gV..
# 
# 
# __ ______ __ ______
#     ?
