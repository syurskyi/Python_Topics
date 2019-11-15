# -*- coding: utf-8 -*-

# f_ col__ im__ deg__
#
# c__ Memoized
#     ___ __i_  ___ cache_size_100
#         ___.cache_size _ cache_size
#         ___.call_args_queue = deque__
#         ___.call_args_to_result = ||
#
#     ___ __c_ self  fn
#         ___ new_func _a__ __k__
#             memoization_key _ s__._convert_call_arguments_to_hash a__ k__
#             i_ me000_k00 n__ i__ ____.call_args_to_result
#                 result _ fn _a__ __k__
#                 ____._update_cache_key_with_value(memoization_key, result)
#                 ___._evict_cache_if_necessary()
#             r_ ____.call_args_to_result[memoization_key]
#         r_ new_func
#
#     ___ _update_cache_key_with_value ____ key value
#         ____.call_args_to_result |key| _ value
#         _____.call_args_queue.ap___ key
#
#     ___ _evict_cache_if_necessary _s___
#         i_ le_ ____.call_args_queue > ____.cache_size
#             oldest_key _ ____.call_args_queue.popleft
#             del ____.call_args_to_result|oldest_key|
#
#     _s__me__
#     ___ _convert_call_arguments_to_hash a___ k___
#         r_ h___ s_ a__ + s__ kwargs
#
#
# _M__ cache_size_5
# ___ get_not_so_random_number_with_max max_value
#     im_ ra___
#     r_ r00.r00__ * m00_v00000