# ____ c.. _______ C..
# ____ c__ _______ D..
# ____ __ _______ p..
# ____ u__.r.. _______ u..
#
# DATA p...j..('/tmp', 'bite_output_log.txt')
# __ n.. p...i.. ?
#     u..('https://bit.ly/2HoFZBd' ?
#
#
# c_ BiteStats
#
#     ___ _load_data  data __ l..
#         w__ o.. ? __ d
#             r.. l.. ? ?
#
#     ___ -  data_?
#         rows _? ?
#
#     ___ _count_attribute  attrib completed=F..
#         r.. C.. x a.. ___ ? __ rows __ n.. completed o. c.. a.. x 'completed'  __ 'True'
#
#     ___ _count_clicks  attrib completed=F..
#         counter C..
#         ___ x __ r..
#             __ n.. c.. o.  c.. a.. x 'completed'  __ 'True'
#                 c.. ? a.. +_ 1
#         r.. ?
#
#     $
#     ___ number_bites_accessed - __ i..
#         """Get the number of unique Bites accessed"""
#         r.. l.. _? 'bite' .i..
#
#     $
#     ___ number_bites_resolved - __ i..
#         """Get the number of unique Bites resolved (completed=True)"""
#         r.. l.. _? 'bite' T.. .i..
#
#     $
#     ___ number_users_active - __ i..
#         """Get the number of unique users in the data set"""
#         r.. l.. _? 'user' .i..
#
#     $
#     ___ number_users_solving_bites - __ i..
#         """Get the number of unique users that resolved
#            one or more Bites"""
#         r.. l.. _? 'user' T.. .i..
#
#     $
#     ___ top_bite_by_number_of_clicks - __ s..
#         """Get the Bite that got accessed the most
#            (= in most rows)"""
#         r.. _? 'bite' .m.. 0 0
#
#     $
#     ___ top_user_by_bites_completed - __ s..
#         """Get the user that completed the most Bites"""
#         r.. _? 'user' T.. .m.. 0 0
#
