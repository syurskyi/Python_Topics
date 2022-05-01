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
#
#
#         w__ o.. ? _ __ f
#             csv_reader ? ? d.._','
#
#             ___ row __ ?
#                 y.. ?
#
#     ___ -  data_?
#         rows l.. _? ?
#
#     $
#     ___ number_bites_accessed - __ i..
#         """Get the number of unique Bites accessed"""
#         bites s..
#         ___ row __ ?
#             ?.a.. ? 'bite'
#
#         r.. l.. ?
#
#     $
#     ___ number_bites_resolved - __ i..
#         """Get the number of unique Bites resolved (completed=True)"""
#         completed s..
#         ___ row __ ?
#             __ ? 'completed'  __ 'True'
#                 ?.a.. ? 'bite'
#         r.. l.. ?
#
#
#     $
#     ___ number_users_active - __ i..
#         """Get the number of unique users in the data set"""
#         users s..
#         ___ row __ ?
#             ?.a.. ? 'user'
#
#         r.. l.. ?
#
#
#     $
#     ___ number_users_solving_bites - __ i..
#         """Get the number of unique users that resolved
#            one or more Bites"""
#         users s..
#
#         ___ row __ f.. l.... row ? 'completed'  __ 'True'
#             ?.a.. ? 'user'
#
#         r.. l.. ?
#
#
#
#     $
#     ___ top_bite_by_number_of_clicks - __ s..
#         """Get the Bite that got accessed the most
#            (= in most rows)"""
#
#
#         r.. C..row 'bite'  ___ ? __ ? .m.. 1 0 0
#
#     $
#     ___ top_user_by_bites_completed - __ s..
#         """Get the user that completed the most Bites"""
#
#         r.. C.. row 'user'  ___ ? __ f.. l.... row ? 'completed'  __ 'True' ?.m.. 1 0 0
#
#
#
# __ _______ __ _______
#
#     l ? ?
#
#     print l.. ?.r..
#