# ____ t___ _______ G..
#
# VALUES "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"
#
#
# ___ calc_sums values s.. ? __ G.. s.. N.. N..
#     """
#     Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.
#
#     The output should be a generator that produces a string that recites the calculation for each pair, for example:
#
#         'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
#     """
#     values_list ?.s.. "[]" .s.. ", "
#     ___ i __ r.. 1 l.. ?
#
#         previous, current f__ ? ? -1 f__ ? ?
#         __ p.. < 0.1 a.. c.. < 0.1
#             total ? + ?
#         ____
#             total r.. ? 2 + r.. ? 2
#
#         y.. _*The sum of ? ? -1 and ? ?, rounded to two decimal places, is ?|.2f
#
#
# # if __name__ == "__main__":
# #     test = calc_sums()
# #     print(next(test))
# #     print(next(test))
# #     print(next(test))
# #     print(next(test))
# #     print(next(test))