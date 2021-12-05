# ______ __
# ______ __
# ____ __.p.. ______ j..
#
# ______ t___
#
# WIND_REGEX = "\d* METAR.*EGLL \d*Z [A-Z ]*(\d{5}KT|VRB\d{2}KT).*="
# WIND_EX_REGEX = "(\d{5}KT|VRB\d{2}KT)"
# VARIABLE_WIND_REGEX = ".*VRB\d{2}KT"
# VALID_WIND_REGEX = "\d{5}KT"
# WIND_DIR_ONLY_REGEX = "(\d{3})\d{2}KT"
# TAF_REGEX = ".*TAF.*"
# COMMENT_REGEX = "\w*#.*"
# METAR_CLOSE_REGEX = ".*="
#
#
# ___ parse_to_array text
#     lines = ?.s...
#     metar_str = ""
#     metars = # list
#     ___ line __ ?
#         __ __.s.. T.. ?
#             _____
#         __ n.. __.s.. C.. ?
#             metar_str += line.s..
#         __ __.s..(M... ?
#             m__.a.. m..
#             m.. = ""
#     r.. m..
#
#
# ___ extract_wind_direction metars
#     winds = # list
#     ___ metar __ ?
#         __ __.s.. W.. ?
#             ___ token __ m__.s..
#                 __ __.m.. W.. t.. w__.a.. __.m.. W.. t.. .g.. 1
#     r.. w..
#
#
# ___ mine_wind_distribution winds wind_dist
#     ___ wind __ ?
#         __ __.s.. V.. ?
#             ___ i __ r... 8
#                 ? ? += 1
#         ____ __.s.. V.. ?
#             d = i.. __.m.. W.. ? .g.. 1
#             dir_index = r..(d / 45.0) % 8
#             ? ? += 1
#     r.. w..
#
#
# __ _____ __ _____
#     path_with_files = "../metarfiles"
#     wind_dist = [0] * 8
#     start = t___.t___
#     ___ file __ __.l.. ?
#         f = o.. j.. ? ? _  # read
#         text = ?.r..
#         metars = p.. ?
#         winds = e.. ?
#         wind_dist = m.. ? ?
#     end = t___.t___
#     print ?
#     print("Time taken", ? -  ?