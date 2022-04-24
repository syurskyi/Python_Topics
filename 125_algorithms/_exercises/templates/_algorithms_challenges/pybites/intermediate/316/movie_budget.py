# ____ d__ _______ date
# ____ t___ _______ D.. S.. N.
#
#
# c_ ? N..
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
# ___ rent_or_stream
#     renting_history ?
#     streaming_cost_per_month i.. ?
#  __ D.. s.. s..
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
#     movie_history    # dict
#     ___ movie __ ?
#         movie_date ?.d__.s.. _Y-_m
#         __ ? n.. __ ?
#             ? ? ?.p..
#         ____
#             ? ?.a.. ?
#
#     ___ key value __ ?.i..
#         __ s.. v.. <_ ?
#             ? k.. "rent"
#         ____
#             ? k.. "stream"
#
#     r.. ?
#
#
# __ _______ __ _______
#     r.. ? 'Mad Max Fury Road', 4, ? 2020, 12, 17,
#      ? 'Die Hard', 4, ? 2020, 12, 3,
#      ? 'Wonder Woman', 4, ? 2020, 12, 28])