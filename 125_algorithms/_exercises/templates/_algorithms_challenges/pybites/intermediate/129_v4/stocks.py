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
#        - if 'B', strip it off and multiple by 1,000 and return
#          value as float"""
#
#     __ 'n/a' __ ?
#         value 0
#     ____
#         unit ? -1
#         cap ? 1|-1
#         value f__ ?
#         value ? * 1000 __ ? __ 'B' ____ ?
#
#     r.. ?
#
#
# ___ get_industry_cap industry
#     """Return the sum of all cap values for given industry, use
#        the _cap_str_to_mln_float to parse the cap values,
#        return a float with 2 digit precision"""
#     total s.. m.. l.... x ? ? 'cap'
#                     f.. l.... x ? 'industry'  __ ? d..
#
#
#
#     r.. r.. ? 2
#
#
# ___ get_stock_symbol_with_highest_cap
#     """Return the stock symbol (e.g. PACD) with the highest cap, use
#        the _cap_str_to_mln_float to parse the cap values"""
#     r.. m.. ? k.._l.... x ? ? 'cap'  'symbol'
#
#
# ___ get_sectors_with_max_and_min_stocks
#     """Return a tuple of the sectors with most and least stocks,
#        discard n/a"""
#     min_max C.. m.. l.... x ? 'sector'
#                           f.. l.... x ? 'sector'  !_ 'n/a' d..
#
#
#     most ?.m.. 1 0 0
#     least ?.m.. -1 0
#     r.. ? ?
