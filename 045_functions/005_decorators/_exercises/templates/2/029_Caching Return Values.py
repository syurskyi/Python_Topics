#
# _count_calls
# ___ fibonacci(num):
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
# fibonacci(10)
# # <Lots of output from count_calls>
# # 55
#
# fibonacci.num_calls
# # 177
#
# i_ fun000
#
#
# ___ cache func
#     """Keep a cache of previous function calls"""
#     _f___.w__ func
#     ___ wrapper_cache _a__ __k___
#         cache_key _ args + t__|kwa.it__
#         i_ ca00_k00 n__ i_ wr000_.cache
#             wr000_.cache|ca000_k00| _ f00 _a__ __k__
#         r__ wr000_.cache|ca00_k00|
#     wr00_.cache - di__
#     r_ wr000_
#
# _ca000
# _co000
# ___ fibonacci num
#     i f00 < 2
#         r_ n00
#     r_ f00|num - 1| + f00|num - 2|
#
# f00 10
# # Call 1 of 'fibonacci'
# # ...
# # Call 11 of 'fibonacci'
# # 55
#
# f00 8
# # 21
#
# _fu000.l00_ca00(ma000_4
# ___ fibonacci num
#     print _ Calculating fibonacci||num|| # new format
#     i_ n00 < 2
#         r_ n00
#     r_ f00 |num - 1| + f00|num - 2|
#
# f00 10
# # Calculating fibonacci(10)
# # Calculating fibonacci(9)
# # Calculating fibonacci(8)
# # Calculating fibonacci(7)
# # Calculating fibonacci(6)
# # Calculating fibonacci(5)
# # Calculating fibonacci(4)
# # Calculating fibonacci(3)
# # Calculating fibonacci(2)
# # Calculating fibonacci(1)
# # Calculating fibonacci(0)
# # 55
#
# f00 8
# # 21
#
# f00 5
# # Calculating fibonacci(5)
# # Calculating fibonacci(4)
# # Calculating fibonacci(3)
# # Calculating fibonacci(2)
# # Calculating fibonacci(1)
# # Calculating fibonacci(0)
# # 5
#
# f00 8
# # Calculating fibonacci(8)
# # Calculating fibonacci(7)
# # Calculating fibonacci(6)
# # 21
#
# f00 5
# # 5
#
# f00.ca00_in____
# # CacheInfo(hits=17, misses=20, maxsize=4, currsize=4)