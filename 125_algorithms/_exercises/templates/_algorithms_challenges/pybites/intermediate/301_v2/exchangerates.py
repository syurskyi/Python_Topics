# _______ __
# _______ j__
# ____ d__ _______ d..
# _______ d__ __ dt
# ____ p.. _______ P..
# ____ t___ _______ D.. L..
# ____ u__.r.. _______ u..
# ____ dateutil.p.. _______ p..
#
# URL "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
# TMP P.. __.g.. "TMP", "/tmp"
# RATES_FILE ? / "exchangerates.json"
#
# __ n.. ?.e..
#     u.. ? ?
#
#
# ___ get_all_days start_date ? end_date ? __ L.. ?
#
#     dates    # list
#
#     current_date start_date
#     w.... ? !_ e..
#         ?.a.. ?
#         ? +_ dt.t.. d.._1
#
#
#     ?.a.. ?
#
#     r.. ?
#
#
#
#
#
# ___ match_daily_rates start d.. end d.. daily_rates d.. __ D.. ? ?
#
#
#
#
#     dates s.. ?.k..
#
#
#
#     i 0
#     w.... ? < l.. ? a.. p.. ? ?.d.. < s..
#         ? +_ 1
#
#
#
#     mapping    # dict
#
#     current_date start
#
#     w.... i < l.. d..
#         date p.. d.. ?.d..
#         __ ? __ ?
#             ? ? ?
#             ? +_ ?.t.. d.._1
#             i +_ 1
#         ____ ? > c..
#             ? ? p.. d.. ? -1 .d..
#             c.. +_ ?.t.. d.._1
#         ____
#             ? +_ 1
#
#
#     r.. ?
#
#
#
# ___ exchange_rates
#     start_date s.. "2020-01-01", end_date s.. "2020-09-01"
#  __ D.. d.. d..
#
#
#     w__ o.. ? _ __ f
#         data j__.l.. ?
#     __ s.. < ? 'start_at'  o. e.. > ? 'end_at'
#         r.. V...("Invalid dates")
#     matching_dates m.. p.. s__ .d.. p.. e__ .d.. ? 'rates'
#
#
#     result    # dict
#     ___ date_1,date_2 __ m__.i..
#         date ?_2.s.. _Y-_m-_d
#         value 'Base Date': ?_2'USD': d.. 'rates' ? 'USD' ,'GBP' d.. 'rates' ? 'GBP'
#         ? ?_1 ?
#
#     r.. ?
#
# __ _______ __ _______
#
#     ?
#
