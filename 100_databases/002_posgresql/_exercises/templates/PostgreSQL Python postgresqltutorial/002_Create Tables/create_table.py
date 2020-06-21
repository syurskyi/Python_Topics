# _____ ?
# ____ c.. _____ c..
#
#
# ___ create_tables
#     """ create tables in the PostgreSQL database"""
#     commands _ (
#         """
#         C.. T.. vendors (
#             vendor_id S.. P.. K..
#             vendor_name V..(255) N.. N..
#         )
#         """,
#         """ C.. T.. parts (
#                 part_id S.. P.. K..
#                 part_name V..(255) N.. N..
#                 )
#         """,
#         """
#         C.. T.. part_drawings (
#                 part_id IN.. P.. K..
#                 file_extension V..(5) N.. N..
#                 drawing_data BYTEA N.. N..
#                 F.. K.. (part_id)
#                 R.. parts (part_id)
#                 O. U.. CA.. O. D.. CA..
#         )
#         """
#         """
#         C.. T.. vendor_parts (
#                 vendor_id IN.. N.. N..
#                 part_id IN.. N.. N..
#                 P.. K.. (vendor_id  part_id)
#                 F.. K.. (vendor_id)
#                     R.. vendors (vendor_id)
#                     O. U.. CA.. O. D.. CA..
#                 F.. K.. (part_id)
#                     R.. parts (part_id)
#                     O. U.. CA.. O. D.. CA..
#         )
#         """)
#     conn _ N..
#     ___
#         # read the connection parameters
#         params _ c..
#         # connect to the PostgreSQL server
#         conn _ ?.c.. $$p..
#         cur _ ?.c..
#         # create table one by one
#         ___ command __ ?
#             ?.e.. ?
#         # close communication with the PostgreSQL database server
#         ?.c..
#         # commit the changes
#         ?.c..
#     ______ E.. ?.DE.. __ error
#         print ?
#     f__
#         __ ? __ no. N..
#             ?.c..
#
#
# __ _____ __ ______
#     ?