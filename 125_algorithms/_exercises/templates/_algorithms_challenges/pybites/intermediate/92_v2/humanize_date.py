# ____ c.. _______ n..
# ____ d__ _______ d__
#
# TimeOffset n..('TimeOffset', 'offset date_str divider')
#
# NOW d__.n..
# MINUTE, HOUR, DAY 60, 60*60, 24*60*60
# TIME_OFFSETS
#     T..  10, 'just now', N..
#     T..  M.. , '@ seconds ago', N..
#     T..  2*M.. , 'a minute ago', N..
#     T..  H.. , '@ minutes ago', M..
#     T..  2*H.. , 'an hour ago', N..
#     T..  DAY, '@ hours ago', H..
#     T..  2*DAY, 'yesterday', N..
#
#
#
# ___ pretty_date date
#     """Receives a datetime object and converts/returns a readable string
#        using TIME_OFFSETS"""
#
#
#     __ t.. ?!_ d__
#         r.. V... "Not a datetime"
#
#     __ ? > N..
#         r.. V... "Invalid date! Date in future!"
#
#
#     delta i.. N..  - ? .t..
#
#
#     ___ time_offset,time_string,divider __ T..
#         __ ? < t..
#             __ d..
#                 d.. //= d..
#
#
#             __ '@' __ t..
#                 r.. t__.f.. ?
#             ____
#                 r.. ?
#
#
#     r.. ?.s.. _m/_d/_y
