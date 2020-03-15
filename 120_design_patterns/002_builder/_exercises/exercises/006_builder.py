# # Version 2.0
# #=======================================================================================================================
# ____ a.. ______ A... a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Toy m..
#     """toy"""
#
#     ___ - name
#         _?  ?
#         __components _     # list
#
#     ___ getName
#         r_ _n..
#
#     ___ addComponent  component count _ 1 unit _ "Each"
#         __c__.ap.. ? ? ?
#         # print("%s increased %d %s%s" % (self._name, count, unit, component) );
#
#     ??
#     ___ feature
#         p..
#
#
# c_ Car
#     """Trolley"""
#
#     ___ feature
#         print("I'm @, I can run fast ..."  _n...
#
#
# c_ Manor T..
#     """manor"""
#
#     ___ feature
#         print("I'm  %s, I can watch it, and I can also play!" % self._name)
#
#
# c_ ToyBuilder m..
#     """Toy builder"""
#
#     ??
#     ___ buildProduct
#         p..
#
#
# c_ CarBuilder T..
#     """Construction class of car"""
#
#     ___ buildProduct
#         car _ C..("Mini car")
#         print("Building @ ....."  ?.g..
#         ?.aC.. "wheel", 4
#         ?.aC.. "Bodywork", 1
#         ?.aC.. "engine", 1
#         ?.aC.. "steering wheel"
#         r_ ?
#
#
# c_ ManorBuilder T..
#     """Manor Construction"""
#
#     ___ buildProduct
#         manor _ M.. ("Taotao Small Manor")
#         print("Building @ ...."  ?.g..
#         ?.aC.. 'living room', 1, "between"
#         ?.aC.. 'bedroom', 2, "between"
#         ?.aC.. "study", 1, "between"
#         ?.aC.. "kitchen", 1, "between"
#         ?.aC.. "garden", 1, "Each
#         ?.aC.. "Fence", 1, "Blocking")
#         r_ >
#
# c_ BuilderMgr
#     """Construction Management"""
#
#     ___ -
#         __carBuilder _ C..
#         __manorBuilder _ M..
#
#     ___ buildCar  num
#         count _ 0
#         products _     # list
#         w__(c... < n..
#             car _ __cB__.bP..
#             p__.ap.. ?
#             c.. +_1
#             print("Construction completed @ Car @"  c.. c__.gN..
#         r_ ?
#
#     ___ buildManor  num
#         count _ 0
#         products _       # list
#         w___ c.. < n..
#             manor _ __mB__.bP..
#             p__.ap.. ?
#             c.. +_ 1
#             print("Construction completed @ Each @"  c.. m__.gN...
#         r_ ?
#
#
# # Test
# # ==============================
# ___ testAdvancedBuilder
#     builderMgr _ B..
#     ?.bM.. 2
#     print()
#     ?.bC.. 4
#
#
# # testBuilder()
# testAdvancedBuilder()
