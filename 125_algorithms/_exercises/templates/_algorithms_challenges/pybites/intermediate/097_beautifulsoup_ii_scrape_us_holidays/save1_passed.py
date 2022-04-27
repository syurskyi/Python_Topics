# ____ c.. _______ d..
# _______ __
# ____ u__.r.. _______ u..
#
# ____ ___ _______ B..
#
#
# # prep data
# tmp  __.g.. TMP  /tmp
# page 'us_holidays.html'
# holidays_page __.p...j.. ? ?
# u..
#     _*https://bites-data.s3.us-east-2.amazonaws.com/{page}',
#     ?
#
#
# w__ o.. ? __ f
#     content f.r..
#
# holidays d.. l..
#
#
# ___ get_us_bank_holidays content_?
#     """Receive scraped html output, make a BS object, parse the bank
#        holiday table (css class = list-table), and return a dict of
#        keys -> months and values -> list of bank holidays"""
#
#     soup B.. ? 'html.parser'
#     right_table ?.f.. 'table', {'class': 'list-table'})
#
#     dates    # list
#     ___ row __ right_table.f.. 'time'
#         ?.a.. ?.t.. 5|7
#
#     holiday    # list
#     ___ row __ ?.f.. 'a'
#         ?.a.. ?.t__.s..
#
#     l z.. ? ?
#
#     ___ k v __ l
#         h.. ? .a.. ?
#
#     r.. ?