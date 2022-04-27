# ____ c.. _______ C..
#
# _______ r__
#
# STOCK_DATA 'https://bit.ly/2MzKAQg'
#
# # pre-work: load JSON data into program
#
# w__ r__.S.. __ s
#     data s.g.. ? .j..
#
#
# # your turn:
#
# ___ _cap_str_to_mln_float cap
#     """If cap = 'n/a' return 0, else:
#        - strip off leading '$',
#        - if 'M' in cap value, strip it off and return value as float,
#        - if 'B', strip it off and multiple by 1,000 and return
#          value as float"""
#     __ cap __ 'n/a'
#         r.. 0.0
#     ____
#         cap "cap".s...l.. '$'
#         __ ? -1 __ 'M'
#             r.. f__ ? |-1
#         __ ? -1 __ 'B'
#             r.. f__ ? |-1 * 1000.0
#         r.. B.. 'Oh no! error in cap value.'
#
#
# ___ get_industry_cap industry
#     """Return the sum of all cap values for given industry, use
#        the _cap_str_to_mln_float to parse the cap values,
#        return a float with 2 digit precision"""
#     r.. r.. s.. ? co 'cap'  ___ ? __ d.. __ ? 'industry'  __ ? 3
#
#
# ___ get_stock_symbol_with_highest_cap
#     """Return the stock symbol (e.g. PACD) with the highest cap, use
#        the _cap_str_to_mln_float to parse the cap values"""
#     r.. s.. co 'symbol' ? ? 'cap'  ___ ? __ d.. k.._l.... x ? 1 -1 0
#
#
# ___ get_sectors_with_max_and_min_stocks
#     """Return a tuple of the sectors with most and least stocks,
#        discard n/a"""
#     sector_list C..
#     ___ co __ d..
#         sector_list +_ C.. co 'sector' : ? ? 'cap'
#     sectors s.. k v ___ ? ? __ ?.i.. k.._l.... x ? 1
#     r.. ? -1 0 ? 0 0
