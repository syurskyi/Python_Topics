# ______ u__
#
# ____ s.. ______ S..
#
# c_ StackTestCase ?.?
#     ___ test_is_empty_true
#         test_obj _ ?
#         aE.. T.., ?.i..
#
#     ___ test_is_empty_false
#         test_obj _ ?
#         ?.p.. 'data'
#         aE.. F.. ?.i..
#
#     ___ test_pop_handles_empty_stack
#         test_obj _ ?
#         aE.. N.. ?.p..
#         aE.. T.. ?.i..
#
#     ___ test_pop_pops_1_item_stack
#         test_obj _ ?
#         test_data _ 'data1'
#         ?.p.. ?
#         aE.. ? ?.p..
#         aE.. T.. ?.i..
#
#     ___ test_pop_in_correct_order_from_2_item_stack
#         test_obj _ ?
#         test_data1 _ 'data1'
#         test_data2 _ 'data2'
#         ?.p.. _1
#         ?.p.. _2
#         aE.. _2 ?.p..
#         aE.. F.. ?.i..
#         aE.. _1 ?.p..
#         aE.. T.. ?.i..
#
#     ___ test_peek_handles_empty_stack
#         test_obj _ ?
#         aE.. N.. ?.p..
#         aE.. T.. ?.i..
#
#     ___ test_peek_shows_item_in_1_item_stack
#         test_obj _ ?
#         test_data _ 'data1'
#         ?.p.. ?
#         aE.. ? ?.p..
#         aE.. F.. ?.i..
#
#     ___ test_peek_shows_top_of_2_item_stack
#         test_obj _ ?
#         test_data1 _ 'data1'
#         test_data2 _ 'data2'
#         ?.p.. _1
#         ?.p.. _2
#         aE.. _2 ?.p..
#         aE.. F.. ?.i..
#         aE.. _2 ?.p..
#
#     ___ test_size_handles_empty_stack
#         test_obj _ ?
#         aE.. 0 ?.s..
#         aE.. T.. ?.i..
#
#     ___ test_size_returns_1_for_1_item_stack
#         test_obj _ ?
#         test_data _ 'data1'
#         ?.p.. ?
#         aE.. 1 ?.s..
#         aE.. F.. ?.i..
#
#     ___ test_size_returns_correct_number_for_many_item_stack
#         test_obj _ ?
#         test_data0 _ 'data0'
#         test_data1 _ 'data1'
#         test_data2 _ 'data2'
#         test_data3 _ 'data3'
#         test_data4 _ 'data4'
#         test_data5 _ 'data5'
#         test_data6 _ 'data6'
#         test_data7 _ 'data7'
#         test_data8 _ 'data8'
#         test_data9 _ 'data9'
#         ?.p.. _0
#         ?.p.. _1
#         ?.p.. _2
#         ?.p.. _3
#         ?.p.. _4
#         ?.p.. _5
#         ?.p.. _6
#         ?.p.. _7
#         ?.p.. _8
#         ?.p.. _9
#         aE.. 10 ?.s..
#
# __ _____ __ _____
#     ?.?
