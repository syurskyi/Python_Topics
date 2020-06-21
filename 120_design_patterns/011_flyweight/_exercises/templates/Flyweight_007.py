# #=======================================================================================================================
# ______ l....
# # Introduce logging module to record exceptions
#
# c_ Pigment
#     """pigment"""
#
#     ___  -  color
#         __?  ?
#         __user _ ""
#
#     ___ getColor
#         r_ __c..
#
#     ___ setUser user
#         __?  ?
#         r_ ?
#
#     ___ showInfo
#         print("@ get @ color pigment"   __u.. __c..
#
# c_ PigmengFactory
#     """Data Factory Class"""
#
#     ___ -
#         __sigmentSet _ |
#             "red": P... *r..
#             "yellow": P... *y..
#             "blue": P... *b..
#             "green": P... *g..
#             "purple": P... *p..
#         |
#
#     ___ getPigment color
#         pigment _ __s____.ge. ?
#         __ ? __ N..
#             l_____.er.. "No @ Color！" ?
#         r_ ?
#
#
# # Version 2.0
# #=======================================================================================================================
# # Code framework
# #==============================
# ____ a.. ________ A.. a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Flyweight m..
#     """Flyweight Class"""
#
#     ??
#     ___ operation extrinsicState
#         p..
#
# c_ FlyweightImpl F..
#     """Concrete implementation class of Flyweight class"""
#
#     ___  -  color
#         __?  ?
#
#     ___ operation extrinsicState
#         print("@ Get @ Color pigment"  ? __c..
#
# c_ FlyweightFactory:
#     """Flyweight Factory"""
#
#     ___ -
#         __flyweights _   # dict
#
#     ___ getFlyweight key
#         pigment _ __f___.ge. ?
#         __ ? _ N..
#             ? _ F.. ?
#         r_ ?
#
# # Framework-based implementation
# #==============================
#
#
# # Test
# #=======================================================================================================================
# ___ Pigment
#     factory _ P..
#     pigmentRed _ f___.gP... *r.. .sU..("Dream team")
#     ?.showInfo()
#     pigmentYellow _ f___.gP... *y.. .sU..("Dream team")
#     ?.sI..
#     pigmentBlue1 _ f___.gP... *b.. .sU..("Dream team")
#     ?.sI..
#     pigmentBlue2 _ f___.gP... *b.. .sU..("Peace corps")
#     ?.sI..
#
#
# ___ Flyweight(
#     factory _ F..
#     pigmentRed _ f___.gF... *r..
#     ?.o...("Dream team")
#     pigmentYellow _ f___.gF... *y..
#     ?.o...("Dream team")
#     pigmentBlue1 _ f___.gF... *b..
#     ?.o...("Dream team")
#     pigmentBlue2 _ f___.gF... *b..
#     ?.o...("Peace corps")
#
#
# # print("Blue1:" + str(id(pigmentBlue1)) + ", Bule2:" + str(id(pigmentBlue2))
# #       + ", Blue1==Blue2:" + str(pigmentBlue1 == pigmentBlue2))
#
#
#
# # Pigment()
# Flyweight()
