# # ch4/example2.py
#
# ____ th.. ______ L..
#
# my_lock _ L..
#
# # induces deadlocks
# ___ get_data_from_file_v1 filename
#     ?.a..
#
#     w__ o.. f.. _ __ f
#         d__.ap.. ?.r..
#
#     ?.r..
#
# # handles exceptions
# ___ get_data_from_file_v2 filename
#     w__ ? o.. ? _ __ f
#         d__.ap.. f.r..
#
# data _    # list
#
# ___
#     get_data_from_file_v1 'output2/sample0.txt'
#     #get_data_from_file_v2('output2/sample0.txt')
# ______ F..
#     print('File could not be found...')
#
# ?.a..
# print('Lock can still be acquired.')
