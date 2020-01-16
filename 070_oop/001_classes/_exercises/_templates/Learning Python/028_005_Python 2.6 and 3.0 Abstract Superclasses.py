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
# ____ a.. _______ A.. a..
#
# c_ Super _______ _ ____
#     ___ delegate ____
#         ____.action
#    ?a..
#     ___ ? ____
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
