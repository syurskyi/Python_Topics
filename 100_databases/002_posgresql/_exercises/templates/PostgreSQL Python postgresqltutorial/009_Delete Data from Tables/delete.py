# #!/usr/bin/python
#
# _____ ?
# ____ c.. _____ c..
#
# ___ delete_part part_id
#     """ delete part by part id """
#     conn _ N..
#     rows_deleted _ 0
#     ___
#         # read database configuration
#         params _ c..
#         # connect to the PostgreSQL database
#         conn _ ?.c.. $$p..
#         # create a new cursor
#         cur _ ?.c..
#         # execute the U..  statement
#         ?.e..("D.. F.. parts W.. part_id = @" p_i.
#         # get the number of updated rows
#         rows_deleted _ ?.r..
#         # Commit the changes to the database
#         ?.c..
#         # Close communication with the PostgreSQL database
#         ?.c..
#     ______ E.. ?.DE.. __ error
#         print ?
#     f__
#         __ c.. __ no. N..
#             ?.c..
#
#     r_ ?
#
# __ _____ __ ______
#     deleted_rows _ ? 2
#     print('The number of deleted rows: ' ?
