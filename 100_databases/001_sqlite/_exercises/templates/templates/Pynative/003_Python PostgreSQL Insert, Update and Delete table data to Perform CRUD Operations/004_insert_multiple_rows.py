# _____ ?
#
# ___ bulkInsert records
#     ___
#         connection _ ?.c.. u.._"syurskyi"
#                                       p.._"1234"
#                                       h.._"127.0.0.1"
#                                       p.._"5432"
#                                       d.._"postgres_db"
#         cursor _ ?.c..
#         sql_insert_query _ """ I.. I.. mobile (id, model, price)
#                            V.. ? ? ? """
#
#         # executemany() to insert multiple rows rows
#         result _ ?.e_m_ ? r..
#         ?.c..
#         print ?.r.., "Record inserted successfully into mobile table"
#
#     ______ E.., ?.Er.. __ error
#         print("Failed inserting record into mobile table @".f.. ?
#
#     f__
#         # closing database connection.
#         __ (c..
#             ?.c..
#             ?.c..
#             print("PostgreSQL connection is closed")
#
# records_to_insert _ [ (4,'LG', 800) , (5,'One Plus 6', 950)]
# ? ?
#
#
# # 2 Record inserted successfully into mobile table
# # PostgreSQL connection is closed