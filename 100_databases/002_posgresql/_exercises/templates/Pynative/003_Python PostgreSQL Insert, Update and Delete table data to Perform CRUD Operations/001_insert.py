# _____ ?
#
# ___
#    connection _ ?.c.. u.._"syurskyi"
#                                   p.._"1234"
#                                   h.._"127.0.0.1"
#                                   p.._"5432"
#                                   d.._"postgres_db"
#    cursor _ ?.c..
#
#    postgres_insert_query _ """ I.. I.. mobile (ID, MODEL, PRICE) V.. (%s,%s,%s)"""
#    record_to_insert _ (5, 'One Plus 6', 950)
#    ?.e.. p.. r..
#
#    ?.c..
#    count _ ?.r..
#    print ? "Record inserted successfully into mobile table")
#
# ______ E.., ?.Er.. __ error
#     __(c..
#         print("Failed to insert record into mobile table" ?
#
# f__
#     #closing database connection.
#     __(c..
#         ?.c..
#         ?.c..
#         print("PostgreSQL connection is closed")
#
#
# #vOutput:
#
# # 1 Record inserted successfully into mobile table
# # PostgreSQL connection is closed