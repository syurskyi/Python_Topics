# ____ d__ _______ date
# ____ t___ _______ D.. S.. N..
# ____ c.. _______ d..
#
# c_ MovieRented N..
#     title: s..
#     price: i..
#     date: date
#
#
# RentingHistory S.. ?
# STREAMING_COST_PER_MONTH 12
# STREAM, RENT 'stream', 'rent'
#
#
# ___ collect_totals renting_history ? __ D.. s.. i..
#     '''Creates a dictionary containing totals per month, with keys
#     YYYY-MM and values (int) of the total cost for that month and year.
#     '''
#     totals d.. l.... 0
#     ___ movie __ ?
#         ? ?.d__.s..( _Y-_m += ?.p..
#     r.. ?
#
#
# ___ rent_or_stream
#     renting_history: R..
#     streaming_cost_per_month: i.. ?
# ) __ D.. s.. s..
#     """Function that calculates if renting movies one by one is
#        cheaper than streaming movies by months.
#
#        Determine this PER MONTH for the movies in renting_history.
#
#        Return a dict of:
#        keys = months (YYYY-MM)
#        values = 'rent' or 'stream' based on what is cheaper
#
#        Check out the tests for examples.
#     """
#     r.. key R.. __ value <_ S.. ____ S..
#             ___ ? ? __ ? ? .i..
