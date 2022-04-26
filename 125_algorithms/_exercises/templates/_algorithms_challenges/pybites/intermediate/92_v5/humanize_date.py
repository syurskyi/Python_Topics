# ____ c.. _______ n..
# ____ d__ _______ d__
#
# TimeOffset n..('TimeOffset', 'offset date_str divider')
#
# NOW d__.n..
# MINUTE, HOUR, DAY 60, 60*60, 24*60*60
# TIME_OFFSETS
#     ? 10, 'just now', N..),
#     ? M.., '@ seconds ago', N..
#     ? 2*M.., 'a minute ago', N..
#     ? H.., '@ minutes ago', M..
#     ? 2*H.., 'an hour ago', N..
#     ? D.., '@ hours ago', H..
#     ? 2*D.., 'yesterday', N..
#
#
#
# ___ pretty_date date d__
#     """Receives a datetime object and converts/returns a readable string
#        using TIME_OFFSETS"""
#     __ n.. isi.. ?, d__ o. ? > N..
#         r.. V...('pretty_date() only accepts datetime objects in the past')
#     diff N.. - ?
#     seconds i.. ?.t..
#     minutes ? // 60
#     hours ? // 60
#     # This doesn't _feel_ very pythonic…
#     __ s.. < 10
#         r.. 'just now'
#     __ s.. < 60
#         r.. _* s.. seconds ago
#     __ m.. < 2
#         r.. 'a minute ago'
#     __ m.. < 60
#         r.. _* m.. minutes ago
#     __ h.. < 2
#         r.. 'an hour ago'
#     __ h.. < 24
#         r.. _* ? hours ago'
#     __ h.. < 48
#         r.. 'yesterday'
#     r.. ?.s.. _m/_d/_y
