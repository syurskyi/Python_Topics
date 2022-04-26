# ____ c.. _______ n..
# ____ d__ _______ d__
#
# TimeOffset n..('TimeOffset', 'offset date_str divider')
#
# NOW d__.n..
# MINUTE, HOUR, DAY 60, 60*60, 24*60*60
# TIME_OFFSETS
#     ? 10, 'just now', N..
#     ? M.., '@ seconds ago', N..
#     ? 2*M.., 'a minute ago', N..
#     ? H.., '@ minutes ago', M..
#     ? 2*H.., 'an hour ago', N..
#     ? D.., '@ hours ago', H..
#     ? 2*D.., 'yesterday', N..
#
#
#
# ___ pretty_date date
#     """Receives a datetime object and converts/returns a readable string
#        using TIME_OFFSETS"""
#     __ n.. isi.. ? d__ o. ? > N..
#         r.. V...
#
#     secs  N.. - ? .t..
#     print _* ?=
#     ___ to __ T..
#         __ ? < ?.o..
#             result ?.d__.f.. i.. s.. / ?.d.. __ ?.d.. ____ 1
#             _____
#     ____
#         result ?.s.. _m/_d/_y
#
#     r.. ?
