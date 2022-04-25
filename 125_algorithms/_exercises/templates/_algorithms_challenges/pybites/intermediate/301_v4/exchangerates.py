# _______ __
# ____ d__ _______ date, t..
# ____ p.. _______ P..
# ____ t___ _______ Dict, L.., O..
# ____ u__.r.. _______ u..
# _______ j__
# ____ c.. _______ O..
#
# URL "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
# TMP P.. __.g.. "TMP", "/tmp"
# RATES_FILE TMP / "exchangerates.json"
#
# __ n.. ?.e..
#     u.. ? ?
#
#
# ___ get_all_days start_date ? end_date ? __ L.. ?
#     delta ? - ?
#     r..  ?+t.. d.._x ___ ? __ r.. ?.d.. +1
#
#
# ___ _parse_date date_string s.. __ d..
#     r.. date *m.. i.. ?.s.. '-'
#
#
# """{
#     "start_at": "2019-01-01",
#     "end_at": "2020-09-01",
#     "base": "EUR",
#     "rates": {
#         "2019-06-28": {
#             "USD": 1.138,
#             "GBP": 0.89655
#         },
#         "2020-05-19": {
#             "USD": 1.095,
#             "GBP": 0.89535
#         },
#         "...": {}
#     }
# }"""
#
#
# ___ _date_conv data d..
#     r.. ? k v ___ ? ? __ ?.i..
#
#
# ___ match_daily_rates start d..
#                       end d.. daily_rates d.. __ D.. ? ?
#     keys l.. ?.k..
#     __ isi.. ?0 s..
#         data_days s.. l.. m.. ? ?
#     ____
#         d.. s.. ?
#
#     r_start m.. ?
#     r_end m.. ?
#
#     __ s.. < r_s.. o. e.. < r_e..
#         r.. V...('Date out of range')
#
#     days get_all_days start end
#     result    # dict
#     ___ day __ days
#         __ ? __ ?
#             m.. ?
#         ____
#             closest m.. ? k.._l.... x| a.. ?-? .d..
#             __ ? > ?
#                 m.. d.. ?.i.. ? - 1
#             ____
#                 m.. ?
#         ? ? m..
#
#     r.. ?
#
#
# ___ exchange_rates
#     start_date s.. "2020-01-01", end_date s.. "2020-09-01"
#  __ O..
#     daily_rates _? j__.l.. R__.r.. 'rates'
#     start_date end_date m.. _? ? ?
#     __ ? < m.. ?.k.. o. e.. > m.. d__.k..
#         r.. V... 'Date out of range for data'
#     matches m.. s.. e.. d..
#     result    # dict
#     ___ day, m.. __ ?.i..
#         ? ? "Base Date": m.. $$d.. m..
#
#     r.. ?
