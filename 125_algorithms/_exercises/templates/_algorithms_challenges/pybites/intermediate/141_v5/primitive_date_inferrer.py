# ____ c.. _______ C..
# ____ d__ _______ d__
# ____ e.. _______ E..
#
#
# c_ DateFormat E..
#     DDMMYY 0  # dd/mm/yy
#     MMDDYY 1  # mm/dd/yy
#     YYMMDD 2  # yy/mm/dd
#     NONPARSABLE -999
#
#     ??
#     ___ get_d_parse_formats cls val_ N..
#         """ Arg:
#         val(int | None) enum member value
#         Returns:
#         1. for val=None a list of explicit format strings
#             for all supported date formats in this enum
#         2. for val=n an explicit format string for a given enum member value
#         """
#         d_parse_formats _d/_m/_y _m/_d/_y _y/_m/_d
#         __ val __ N..
#             r.. ?
#         __ 0 <_ val <_ l.. ?
#             r.. ? ?
#         r.. V...
#
#
# c_ InfDateFmtError E..
#     """custom exception when it is not possible to infer a date format
#     e.g. too many NONPARSABLE or a tie """
#     p..
#
#
# ___ _maybe_DateFormats date_str
#     """ Args:
#     date_str (str) string representing a date in unknown format
#     Returns:
#     a list of enum members, where each member represents
#     a possible date format for the input date_str
#     """
#     d_parse_formats ?.g..
#     maybe_formats    # list
#     ___ idx d_parse_fmt __ e.. ?
#         ___
#             _parsed_date d__.s.. ? ?  # pylint: disable=W0612
#             ?.a.. ? i..
#         ______ V..
#             p..
#     __ l.. ? __ 0:
#         ?.a.. ?.N..
#     r.. ?
#
#
# ___ get_dates dates
#     """ Args:
#     dates (list) list of date strings
#     where each list item represents a date in unknown format
#     Returns:
#     list of date strings, where each list item represents
#     a date in yyyy-mm-dd format. Date format of input date strings is
#     inferred based on the most prevalent format in the dates list.
#     Alowed/supported date formats are defined in a DF enum class.
#     """
#     result    # list
#     fmts C.. maybe ___ dt __ ? ___ ? __ _? __.m.. 2
#     __ fmts 0 0  __ ?.N.. o. ? 0 1 __ ? 1 1
#         r.. I..
#     fmt ?.g..? 0 0 .v..
#
#     ___ dt __ ?
#         ___
#             r__.a.. d__.s.. ? ? .s.. _Y-_m-_d
#         ______ V..
#             r__.a.. 'Invalid'
#
#     r.. ?
