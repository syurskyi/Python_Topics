# _______ __
# _______ j__
# ____ d__ _______ d__ d.. t..
# ____ p.. _______ P..
# ____ t___ _______ D.. L..
# ____ u__.r.. _______ u..
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
#     date_diff (? - ?).d..
#     current_date s..
#
#     ___ _ __ r.. ? +1
#         ?.a.. ?
#         c.. ? + t.. d.._1
#
#     r.. ?
#
#
# ___ match_daily_rates start d.. end d.. daily_rates d.. __ D.. ? ?
#
#     dates_open_lookup s.. m.. l.... x| d__.s.. ? _Y-_m-_d .d.. ?
#
#     dates    # dict
#     date_diff (? - ?).d..
#     current_date s..
#     ___ i __ r.. ? +1
#         previous_date ?
#         __ c.. n.. __ d..
#             w.... ? n.. __ d..
#                 p.. ? - t.. d.._1
#             d.. c.. p...
#             c.. ? + t.. d.._1
#         ____
#             d.. c.. c..
#             c.. c.. + t.. d.._1
#
#     r.. ?
#
#
# ___ exchange_rates
#     start_date s.. "2020-01-01" end_date s.. "2020-09-01"
#  __ D.. d.. d..
#
#     w__ o.. ? __ file
#         data j__.l.. ?
#
#     start d__.s.. ? _Y-_m-_d .d..
#     end d__.s.. ? _Y-_m-_d .d..
#
#     __ s.. < d__.s.. d.. "start_at" _Y-_m-_d .d.. o. e.. > d__.s.. d.. "end_at" _Y-_m-_d .d..
#         r.. V...("Invalid start date or end date"
#
#     dates ? ? ? ? "rates"
#
#     result    # dict
#     ___ key value __ ?.i..
#         temp_dict    # dict
#         date_string v__.s.. _Y-_m-_d"
#         ? "Base Date" v...
#         ?.u.. d.. "rates" ?
#         ? ? t.. #data["rates"][date_string]
#
#     r.. ?
#
#
# # if __name__ == "__main__":
# #     start_date = date(2020, 4, 9)
# #     end_date = date(2020, 4, 14)
# #     get_all_days(start_date, end_date)
# #     print(exchange_rates("2020-04-09", "2020-04-14"))