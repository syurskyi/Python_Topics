# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# *References:
# http://codesnipers.com/?q_python-flyweights
#
# *TL;DR80
# Minimizes memory usage by sharing data with other similar objects.
# """
#
# ______ w...
#
#
# c_ FlyweightMeta ty..
#
#     ___ -n mcs name parents dct
#         """
#         Set up object pool
#
#         :param name: class name
#         :param parents: class parents
#         :param dct: dict: includes class attributes, class methods,
#         static methods, etc
#         :return: new class
#         """
#         d.. |'pool' + w___.WVD..
#         r s___ F... m__ . -n ?  ?  ?  ?
#
#     ??
#     ___ _serialize_params ___ $ $$
#         """
#         Serialize input parameters to a key.
#         Simple implementation is just to serialize it as a string
#         """
#         args_list _ li.. ma. st. a..
#         ?.ex.. st. kw.. ___. -n||
#         key _ ''.jo.. ?
#         r ?
#
#     ___-c ___ $ $$
#         key _ F___._s_p.. ___ $ $$
#         pool _ ge.. ___ *p..  ||
#
#         instance _ p___.ge. k..
#         __ ? __ N..
#             instance _ s___ F... ___ . -c $ $$
#             po..|k.. _ ?
#         r ?
#
#
# c_ Card o..
#
#     """The object pool. Has builtin reference counting"""
#     _CP.. _ w___.WVD..
#
#     """Flyweight implementation. If the object exists in the
#     pool just return it (instead of creating a new one)"""
#     ___ -n ___ value suit
#         obj _ C__._CP__.ge. ? + ?
#         __ no. ?
#             ? _ obj___. n ___
#             C___._CP..|? + ? _ ?
#             ?.v.. ?.s.. _ ? ?
#         r ?
#
#     # ___ __init__(self, value, suit):
#     #     self.value, self.suit _ value, suit
#
#     ___ -r
#         r "<Card: @@>"  ?  ?
#
#
# ___ with_metaclass meta $bases
#     """ Provide python cross-version metaclass compatibility. """
#     r ? "NewBase" b.. ||
#
#
# c_ Card2 w_m.. FM..
#
#     ___ - $ $$
#         # print('Init {}: {}'.format(self.__class__, (args, kwargs)))
#         p..
#
#
# __ _______ __ ______
#     # comment __new__ and uncomment __init__ to see the difference
#     c1 _ C..('9', 'h')
#     c2 _ C..('9', 'h')
#     print(c1, c2)
#     print(c1 == c2, c1 is c2)
#     print(id(c1), id(c2))
#
#     c1.temp _ None
#     c3 _ C..('9', 'h')
#     print(hasattr(c3, 'temp'))
#     c1 _ c2 _ c3 _ None
#     c3 _ C..('9', 'h')
#     print(hasattr(c3, 'temp'))
#
#     # Tests with metaclass
#     instances_pool _ getattr(Card2, 'pool')
#     cm1 _ Card2('10', 'h', a_1)
#     cm2 _ Card2('10', 'h', a_1)
#     cm3 _ Card2('10', 'h', a_2)
#
#     assert (cm1 == cm2) !_ cm3
#     assert (cm1 is cm2) is not cm3
#     assert len(instances_pool) == 2
#
#     del cm1
#     assert len(instances_pool) == 2
#
#     del cm2
#     assert len(instances_pool) == 1
#
#     del cm3
#     assert len(instances_pool) == 0
#
# ### OUTPUT ###
# # (<Card: 9h>, <Card: 9h>)
# # (True, True)
# # (31903856, 31903856)
# # True
# # False
