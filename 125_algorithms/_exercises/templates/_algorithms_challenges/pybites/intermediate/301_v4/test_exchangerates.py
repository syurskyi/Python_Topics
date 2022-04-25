# _______ j__
# ____ d__ _______ d..
#
# _______ p__
#
# ____ ? _______ ? ? ? ?
#
#
# ?p__.f.. s.._"session"
# ___ exchange_rates_result
#     r.. ?
#
#
# ?p__.f.. s.._"session"
# ___ matching_result
#     start d.. 2020, 1, 1
#     end d.. 2020, 9, 1
#     daily_rates j__.l..  R__.r.. "rates"
#     r.. ? s.. e.. d..
#
#
# ?p__.m__.p.
#     "start, end, expected",
#
#         (d..(2020, 1, 1), d..(2020, 1, 31), 31),
#         (d..(2020, 1, 14), d..(2020, 1, 29), 16),
#         (d..(2020, 4, 12), d..(2020, 4, 14), 3),
#
#
# ___ test_get_all_days start end  e..
#     a.. ? ? ?
#     ... l.. a.. __ e..
#
#     ... isi.. a.. 0 d..
#     ... isi.. a..-1 d..
#
#     ... a.. 0 __ ?
#     ... a.. -1 __ ?
#
#
# ?p__.m__.p.
#     "d.., expected",
#
#         (d..(2020, 1, 18), d..(2020, 1, 17,
#         (d..(2020, 2, 2), d..(2020, 1, 31,
#         (d..(2020, 5, 3), d..(2020, 4, 30,
#         (d..(2020, 8, 15), d..(2020, 8, 14,
#
#
# ___ test_match_daily_rates d.. e.. matching_result
#     a.. ?
#     ... a.. d.. __ e..
#
#
# ?p__.m__.p.
#     "testdate, expected",
#
#
#             d..(2020, 7, 16),
#             {"Base Date": d..(2020, 7, 16), "GBP": 0.90875, "USD": 1.1414},
#         ),
#         (
#             d..(2020, 7, 17),
#             {"Base Date": d..(2020, 7, 17), "GBP": 0.91078, "USD": 1.1428},
#         ),
#         (
#             d..(2020, 7, 18),
#             {"Base Date": d..(2020, 7, 17), "GBP": 0.91078, "USD": 1.1428},
#
#
#
# ___ test_exchange_rates_sample testdate e.. exchange_rates_result
#     a.. ?
#
#     ... a.. ? "Base Date"] __ e..["Base Date"
#     ... a.. ? "GBP"] __ e..["GBP"
#     ... a.. ? "USD"] __ e..["USD"
#
#
# ___ test_exchange_rates_all_dates exchange_rates_result
#     ... l.. ? __ 245
#
#
# ___ test_exchange_rates_order exchange_rates_result
#     a.. l.. ?.k..
#     e.. s.. ?.k..
#
#     ... a.. __ e..
#
#
# ___ test_exchange_rates_validate_start
#     w__ p__.r.. V...
#         ? s.._"1950-01-01"
#
#
# ___ test_exchange_rates_validate_end
#     w__ p__.r.. V...
#         ? e.._"2050-01-01"