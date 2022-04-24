# ____ d__ _______ date
# ____ t___ _______ Dict, S.., N..
# ____ c.. _______ n..,d..
#
#
#
# MovieRented n.. "MovieRented","title price date"
# '''
# class MovieRented(NamedTuple):
#     title: str
#     price: int
#     date: date
# '''
#
#
# RentingHistory S.. ?
# STREAMING_COST_PER_MONTH 12
# STREAM, RENT 'stream', 'rent'
#
#
# ___ rent_or_stream
#     renting_history ?
#     streaming_cost_per_month i.. ?
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
#
#
#     m d.. i..
#
#
#     ___ movie_rented __ r..
#         month ?.d__.s.. _Y-_m
#         ? ? += ?.p..
#
#
#
#     ___ month cost __ ?.i..
#         __ cost > s..
#             ? ? S..
#         ____
#             ? ? R..
#
#
#     r.. ?
