# '''
# from abc import ABCMeta, abstractmethod
#
# class Super(metaclass=ABCMeta):
#     @abstractmethod
#     def method(self, ...):
#         pass
#
#
#
# class Super:
#     __metaclass__ = ABCMeta
#     @abstractmethod
#     def method(self, ...):
#         pass
# '''
#
#
# f___ a.. _______ A.. a..
#
# c_ Super _______ _ A.
#     ___ delegate ____
#         ____.action
#    0a..
#     ___ action ____
#         p..
#
# X = ?
# # TypeError: Can't instantiate abstract class Super with abstract methods action
#
# c_ Sub ? p_
#
# X = Su.
# # TypeError: Can't instantiate abstract class Sub with abstract methods action
#
# c_ Sub ?
#     ___ action ____ print('spam')
#
# X = S.
# print ?.d..
#
