# _______ r__
# ____ c.. _______ C..
#
# STOCK_DATA 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'
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
#        - if 'B', strip it off, multiply by 1,000 and return
#          value as float"""
#     __ cap __ 'n/a':
#         r.. 0
#
#
#     cap ?.l.. '$'
#     __ 'M' __ ?
#         value f__ ?.r..'M'
#     ____ 'B' __ ?
#         v.. f__ ?.r..'B' * 1000
#
#     r.. ?
#
#
#
# ___ get_industry_cap industry
#     """Return the sum of all cap values for given industry, use
#        the _cap_str_to_mln_float to parse the cap values,
#        return a float with 2 digit precision"""
#
#     total 0
#     ___ company __ d..
#         __ ? 'industry'  __ ?
#             t.. +_ ? ? 'cap'
#
#
#     r.. r.. ? 2
#
#
#
#
# ___ get_stock_symbol_with_highest_cap
#     """Return the stock symbol (e.g. PACD) with the highest cap, use
#        the _cap_str_to_mln_float to parse the cap values"""
#
#     r.. m.. ?k.._l.... x ? ? 'cap'  'symbol'
#
#
# ___ get_sectors_with_max_and_min_stocks
#     """Return a tuple of the sectors with most and least stocks,
#        discard n/a"""
#     counts C..
#
#     ___ company __ d..
#         sector ? 'sector'
#         __ ? !_ 'n/a':
#             ? ?'sector']] += 1
#
#
#     sector_counts ?.m..
#
#     r.. ? 0 0 ,? -1 0
