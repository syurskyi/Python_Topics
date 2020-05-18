# _____ ?
#
# ___ updateTable(mobileId, price):
#     ___
#         connection _ ?.c..(u.._"syurskyi",
#                                       p.._"1234",
#                                       h.._"127.0.0.1",
#                                       p.._"5432",
#                                       d.._"postgres_db")
#
#         cursor _ ?.c..
#
#         print("Table Before updating record ")
#         sql_select_query _ """s.. * f.. mobile w.. id = %s"""
#         ?.e.. ? mI.
#         record _ ?.f_o..
#         print ?
#
#         # Update single record now
#         sql_update_query _ """Update mobile set price = @ w.. id = @"""
#         ?.e.. ? p.. mI.
#         ?.c..
#         count _ ?.r..
#         print ? "Record Updated successfully ")
#
#         print("Table After updating record ")
#         sql_select_query _ """s.. _ f.. mobile w.. id = @"""
#         ?.e.. ? mI..
#         record _ ?.f_o..
#         print ?
#
#     ______ E.., ?.Er.. __ error
#         print("Error in update operation" ?
#
#     f__
#         # closing database connection.
#         __ (c..
#             ?.c..
#             ?.c..
#             print("PostgreSQL connection is closed")
#
# id _ 3
# price _ 970
# ? ? ?