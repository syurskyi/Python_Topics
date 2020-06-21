# ______ w...
#
#
# c_ FlyweightMeta ty..
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
#         d..|*p.. _ w____.WVD..
#         r_ s___. -n ?  ?  ?  ?
#
#     ??
#     ___ _serialize_params ___ $  $$
#         """
#         Serialize input parameters to a key.
#         Simple implementation is just to serialize it as a string
#         """
#         args_list _ li.. ma. st. a..
#         ?.ex.. st. kw.. ___. -n
#         key _ ''.jo.. ?
#         r_ ?
#
#     ___ -c ___ $  $$
#         key _ F____._s.. ___ $  $$
#         pool _ ge.. ___ *p.. ||
#
#         instance _ p___.ge. k..
#         __ ? __ N..
#             ? _ s____ . -c$  $$
#             p...|ke. _ ?
#         r_ ?
#
#
# c_ Card2 m..._F...
#     ___ - $  $$
#         # print('Init {}: {}'.format(self.__class__, (args, kwargs)))
#         p...
#
#
# __ _______ __ ______
#     instances_pool _ ge.. C..2 *p..
#     cm1 _ C__2('10', 'h', a_1)
#     cm2 _ C__2('10', 'h', a_1)
#     cm3 _ C__2('10', 'h', a_2)
#
#     assert (cm1 == cm2) and (cm1 !_ cm3)
#     assert (cm1 is cm2) and (cm1 is not cm3)
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
