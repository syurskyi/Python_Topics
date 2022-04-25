# _______ j__
# ____ d__ _______ date
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
#     start ? 2020, 1, 1
#     end ? 2020, 9, 1
#     daily_rates j__.l.. ?.r.. "rates"
#     r.. ? ? ? ?
#
#
# ?p__.m__.p.
#     "start, end, expected",
#
#         (?(2020, 1, 1), ?(2020, 1, 31), 31),
#         (?(2020, 1, 14), ?(2020, 1, 29), 16),
#
#
#
# ___ test_get_all_days start end e..
#     a.. ? ?
#     ... l.. a.. __ e..
#
#     ... isi.. a.. 0 ?
#     ... isi.. a.. -1 ?
#
#     ... a.. 0 __ ?
#     ... a.. -1 __ ?
#
#
# ?p__.m__.p.
#     "?, expected",
#
#         (?(2020, 1, 18), ?(2020, 1, 17,
#         (?(2020, 2, 2), ?(2020, 1, 31,
#         (?(2020, 5, 3), ?(2020, 4, 30,
#         (?(2020, 8, 15), ?(2020, 8, 14,
#
#
# ___ test_match_daily_rates ? e.. matching_result
#     a.. ?
#     ... a.. ? __ e..
#
#
# ?p__.m__.p.
#     "testdate, expected",
#
#
#             ?(2020, 7, 16),
#             {"Base Date": ?(2020, 7, 16), "GBP": 0.90875, "USD": 1.1414},
#
#
#             ?(2020, 7, 17),
#             {"Base Date": ?(2020, 7, 17), "GBP": 0.91078, "USD": 1.1428},
#
#
#             ?(2020, 7, 18),
#             {"Base Date": ?(2020, 7, 17), "GBP": 0.91078, "USD": 1.1428},
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