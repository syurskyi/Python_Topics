# -*- coding: utf-8 -*-

# f_ col__ im__ deg__
#
# c__ Memoized
#     ___ -  ___ cache_size_100
#         ___.? _ ?
#         ___.call_args_queue = deque__
#         ___.call_args_to_result =    # dict
#
#     ___ __c_ self  fn
#         ___ new_func $ $$
#             memoization_key _ ___._convert_call_arguments_to_hash $ $$
#             i_ ? n__ i_ ____.c_r..
#                 result _ ? $ $$
#                 ____._update_cache_key_with_value m.. r..
#                 ___._evict_cache_if_necessary()
#             r_ ____.c_t | m..
#         r_ ?
#
#     ___ _update_cache_key_with_value ____ key value
#         ____.c_r.. |k.. _ v..
#         _____.c_q__.ap___ k..
#
#     ___ _evict_cache_if_necessary ___
#         i_ le_ ____.c_q_ > ____.ca_s..
#             oldest_key _ ____.c_q___.po_l_
#             del ____.c_r__|?
#
#     _s__me__
#     ___ _convert_call_arguments_to_hash $ $$
#         r_ ha__ st_ ar.. + st_ kw..
#
#
# ?? ca_si.._5
# ___ get_not_so_random_number_with_max max_value
#     ______ ran___
#     r_ ra__.ra____ * ma__