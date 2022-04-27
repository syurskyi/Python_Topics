# ____ c.. _______ d..
# _______ __
# ____ u__.r.. _______ u..
# ____ d__ _______ d__
# ____ ___ _______ B..
#
#
# # prep data
# tmp  __.g.. TMP  /tmp
# page 'us_holidays.html'
# holidays_page __.p...j.. ? ?
# u..
#     _*https://bites-data.s3.us-east-2.amazonaws.com/ ?
#     ?
#
#
# w__ o.. ? __ f
#     content f.r..
#
# holidays d.. l..
#
#
# ___ _parse_date date s..
#     """returns a datetime from parsing dates as formatted in table"""
#     r.. d__.s.. ?.s.. 0 _Y-_m-_d_B
#
#
# ___ _get_table content_? __ l..
#     """returns the cleaned table with datetimes for the dates"""
#     soup B.. ? 'html.parser'
#     raw_table ?.f.. 'table', {'class': 'list-table'})
#     table c.g.. .s.. ___ c __ r.f.. 'td'
#              ___ r __ ?.f.. 'tr'
#     table.p.. 0                # remove header
#     ___ row __ ?
#         ? 1 _p.. ?1
#     r.. ?
#
#
# ___ get_us_bank_holidays content_?
#     """Receive scraped html output, make a BS object, parse the bank
#        holiday table (css class = list-table), and return a dict of
#        keys -> months and values -> list of bank holidays"""
#     table _?
#
#     ___ row __ ?
#         holidays_* r.. 1 .m..|02d .a.. r.. 3.s..
#
#     r.. ?
