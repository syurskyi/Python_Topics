# ____ c.. _______ n..
# ____ d__ _______ date, d__
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
#     date_delta N.. - ?
#     __ >.d.. __ 0
#         __ >.s.. < 10
#             r.. ? 0 .d..
#         ____ >.s.. >_ 10 a.. >.s.. < M..
#             r.. ? 1 .d...f.. >.s..
#         ____ >.s.. >_ M.. a.. >.s.. < 2 * M..
#             r.. ? 2 .d..
#         ____ >.s.. < H..
#             r.. ? 3 .d...f..(>.s.. // M..
#         ____ >.s.. __ H..
#             r.. ? 4 .d..
#         ____ >.s.. > H..
#             r.. ? 5 .d...f.. >.s.. // H..
#     ____
#         __ >.d.. __ 1 a.. >.s.. >_ 0
#             r.. ? 6 .d..
#         ____
#             r.. N.. - > .s.. _m/_d/_y
#
#
# # if __name__ == "__main__":
# #     test_date = datetime.now()
# #     print(pretty_date(test_date))