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
#     _*https://bites-data.s3.us-east-2.amazonaws.com/?
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
#
#     table ?.f.. 'table' c.._"list-table"
#
#     ___ i,row __ e.. ?.f.. 'tr'
#         __ ? __ 0
#             _____
#         date ?.s.. 'td:nth-child(2)' .g.. s..=T..
#         hyphen ?.i.. '-'
#         date ? ?+1|?+ 3
#
#         holiday r__.s.. 'td:nth-child(4)' .g.. s..=T..
#         ? ?.a.. ?
#
#
#     r.. ?
#
#
# __ _______ __ _______
#
#
#     ?
