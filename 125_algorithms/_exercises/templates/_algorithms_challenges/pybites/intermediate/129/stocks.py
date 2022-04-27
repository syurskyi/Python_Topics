# _______ r__, c..
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
#     __ cap __ "n/a"
#         r.. 0
#     ____
#         cap ?.l.. "$"
#         __ ? -1 __ "B"
#             r.. f__ ?.r.. "B" * 1000
#         ____
#             r.. f__ ?.r.. "M"
#
#
# ___ get_industry_cap industry
#     """Return the sum of all cap values for given industry, use
#        the _cap_str_to_mln_float to parse the cap values,
#        return a float with 2 digit precision"""
#     industry_cap_lookup    # dict
#     ___ stock __ d..
#         cap _? ? "cap"
#         __ ? "industry" n.. __ ?
#             ? ? "industry" ?
#         ____
#             ? ? "industry" .a.. ?
#     r.. r.. s.. ? ? 2
#
#
# ___ get_stock_symbol_with_highest_cap
#     """Return the stock symbol (e.g. PACD) with the highest cap, use
#        the _cap_str_to_mln_float to parse the cap values"""
#     highest_cap    # dict
#     ___ stock __ d..
#         cap _? ? "cap"
#         ? ? "symbol" ?
#     r.. m.. ? k.._?.g..
#
#
# ___ get_sectors_with_max_and_min_stocks
#     """Return a tuple of the sectors with most and least stocks,
#        discard n/a"""
#     counter c...C.. stock "sector" ___ ? __ d.. __ ? "sector" !_ "n/a"
#     r..  ?.m.. 0 0 ?.m.. -1 0
#
#
# # if __name__ == "__main__":
# #    print(_cap_str_to_mln_float('n/a'))
# #    print(_cap_str_to_mln_float('$100.45M'))
# #    print(get_industry_cap("Business Services"))
# #    print(get_stock_symbol_with_highest_cap())
# #    print(get_sectors_with_max_and_min_stocks())