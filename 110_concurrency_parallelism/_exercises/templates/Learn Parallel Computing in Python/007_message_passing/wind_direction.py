# ______ __
# ______ __
# ____ _ ______ Pipe
# ____ __.p.. ______ j..
#
# ______ t___
# ____ _.context ______ P..
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
# ___ parse_to_array text_conn metars_conn
#     text = ?.r..
#     w... ? __ n.. N..
#         lines = ?.s...
#         metar_str = ""
#         metars = # list
#         ___ line __ ?
#             __ __.s.. T.. ?
#                 _____
#             __ n.. __.s.. C.. ?
#                 m.. += ?.s..
#             __ __.s.. M.. ?
#                 m__.a.. m..
#                 m.. = ""
#         m...s.. m..
#         text = ?.r..
#     m__.s.. N..
#
#
# ___ extract_wind_direction metars_conn winds_conn
#     metars = m__.r..
#     w... m.. __ n.. N..
#         winds = # list
#         ___ metar __ ?
#             __ __.s.. W.. ?
#                 ___ token __ m__.s..
#                     __ __.m.. W.. ? w__.a.. __.m.. W.. ? .g.. 1
#         w__.s.. w..
#         m.. = m__.r..
#     w__.s.. N..
#
#
# ___ mine_wind_distribution winds_conn wind_dist_conn
#     wind_dist = [0] * 8
#     winds = w__.r..
#     w... w.. __ n.. N..
#         ___ wind __ ?
#             __ __.s.. V.. ?
#                 ___ i __ r... 8
#                     ? ? += 1
#             ____ __.s.. V.. ?
#                 d = i.. __.m.. W.. ? .g.. 1
#                 dir_index = r.. d / 45.0) % 8
#                 w.. ? += 1
#         w... = w__.r..
#     w__.s.. w..
#
#
# __ _____ __ _____
#     text_conn_a, text_conn_b = ?
#     metars_conn_a, metars_conn_b = ?
#     winds_conn_a, winds_conn_b = ?
#     winds_dist_conn_a, winds_dist_conn_b = ?
#     P..(t.._p.. a.._ t.. m.. .s..
#     P..(t.._e.. a.._ m.. w.. .s..
#     P..(t.._m.. a.._ w.. w.. .s..
#     path_with_files = "../metarfiles"
#     start = t___.t___
#     ___ file __ __.l.. ?
#         f = o.. j.. ? ? _   # reasd
#         text = ?.r..
#         t__.s.. ?
#     t__.s.. N..
#     wind_dist = w__.r..
#     end = t___.t___
#     print ?
#     print("Time taken", ? -  ?