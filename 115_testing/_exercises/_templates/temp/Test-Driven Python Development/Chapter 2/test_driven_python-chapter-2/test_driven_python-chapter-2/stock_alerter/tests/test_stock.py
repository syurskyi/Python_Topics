# _____ u__
# ____ d_t_ _____ d_t_
#
# ____ stock _____ St..
#
#
# c_ StockTest ?.?
#     ___ setUp
#         goog _ ? GOOG"
#
#     ___ test_price_of_a_new_stock_class_should_be_None
#         aIN.. ?.p..
#
#     ___ test_stock_update
#         """An update should set the price on the stock object
#
#         We will be  using the `datetime` module for the timestamp
#         """
#         ?.u.. d_t_ 2014, 2, 12), price_10
#         aE.. 10 ?.p..
#
#     ___ test_negative_price_should_throw_ValueError
#         w__ aR.. V..
#             ?.u.. d_t_ 2014, 2, 13), -1
#
#     ___ test_stock_price_should_give_the_latest_price
#         ?.u.. d_t_ 2014, 2, 12), p.._10
#         ?.u.. d_t_ 2014, 2, 13), p.._8.4
#         aAE.. 8.4 ?.p.. d.._0.0001
#
#
# c_ StockTrendTest ?.?
#     ___ setUp
#         goog _ ?"GOOG"
#
#     ___ given_a_series_of_prices prices):
#         timestamps _ d_t_ 2014, 2, 10 d_t_ 2014, 2, 11
#                       d_t_ 2014, 2, 12 d_t_ 2014, 2, 13
#         ___ timestamp, price __ z.. ? ?
#             ?.u.. ? ?
#
#     ___ test_increasing_trend_is_true_if_price_increase_for_3_updates
#         g.. 8, 10, 12
#         aT.. ?.i_i_t..
#
#     ___ test_increasing_trend_is_false_if_price_decreases
#         g.. 8, 12, 10
#         aF.. ?.i_i_t..
#
#     ___ test_increasing_trend_is_false_if_price_equal
#         g.. 8, 10, 10
#         aF.. ?.i_i_t..
