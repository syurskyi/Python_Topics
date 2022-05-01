# ____ c__ _______ D..
# _______ __
# ____ u__.r.. _______ u..
# ____ c.. _______ C..
#
# TMP __.g.. TMP  /tmp
# LOGS 'bite_output_log.txt'
# DATA __.p...j.. ? ?
# S3 'https://bites-data.s3.us-east-2.amazonaws.com'
# __ n.. __.p...i.. ?
#     u.. _*?/? ?
#
#
# c_ BiteStats
#
#     ___ _load_data  data __ l..
#         w__ o.. ? __ f
#             r.. l.. ?
#
#     ___ -  data_?
#         rows _? ?
#
#     $
#     ___ number_bites_accessed - __ i..
#         """Get the number of unique Bites accessed"""
#         r.. l.. bite 'bite'  ___ ? __ ?
#
#     $
#     ___ number_bites_resolved - __ i..
#         """Get the number of unique Bites resolved (completed=True)"""
#         r.. l.. bite 'bite'  ___ ? __ r..
#                     __ ? 'completed'  __ 'True'
#
#     $
#     ___ number_users_active - __ i..
#         """Get the number of unique users in the data set"""
#         r.. l.. bite 'user'  ___ ? __ ?
#
#     $
#     ___ number_users_solving_bites - __ i..
#         """Get the number of unique users that resolved
#            one or more Bites"""
#         r.. l.. bite 'user'  ___ ? __ r..
#                     __ ? 'completed'  __ 'True'
#
#     $
#     ___ top_bite_by_number_of_clicks - __ s..
#         """Get the Bite that got accessed the most
#            (= in most rows)"""
#         counts C.. bite 'bite'  ___ ? __ ?
#         r.. ?.m.. 1 0 0
#
#     $
#     ___ top_user_by_bites_completed - __ s..
#         """Get the user that completed the most Bites"""
#         counts C.. bite 'user'  ___ ? __ r..
#                          __ ? 'completed'  __ 'True'
#         r.. ?.m.. 1 0 0
