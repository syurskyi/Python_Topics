# ____ c.. _______ C..
# _______ c__
# _______ r__
#
#
# CSV_URL 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'
# FMT_STR '{tz:21}| {bar}'
#
#
# ___ get_csv
#     """Use requests to download the csv and return the
#        decoded content"""
#     r.. r__.g.. url=?.c__.d..
#
#
# ___ create_user_bar_chart content
#     """Receives csv file (decoded) content and print a table of timezones
#        and their corresponding member counts in pluses to standard output
#     """
#     rows c__.D.. ?.s..
#     counts s.. C.. r 'tz'  ___ ? __ ? .i..
#                     k.._l.... x| ? 0
#
#     ___ c __ ?
#         print F__.f.. tz_? 0 bar_'+' * ? 1
