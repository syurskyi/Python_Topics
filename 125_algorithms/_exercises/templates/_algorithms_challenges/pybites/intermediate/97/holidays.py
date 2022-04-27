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
#     soup B.. ? "html.parser"
#     holiday_table ?.f.. c.._"list-table"
#     holiday_dates h_date.g..  ___ ? __ ?.s.. "time"
#     holiday_names h_name.g..  ___ ? __ ?.s.. "a"
#     holiday_zip z.. ? ?
#     ___ h_date, h_name __ ?
#         month h__.s..("-" 1
#         h.. m__ .a.. ?.s..
#     r.. ?
#
#
# # if __name__ == "__main__":
# #     print(get_us_bank_holidays())