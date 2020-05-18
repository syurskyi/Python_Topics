# _____ ?
#
# ___
#     connection _ ?.c.. u.._"syurskyi"
#                                   p.._"1234"
#                                   h.._"127.0.0.1"
#                                   p.._"5432"
#                                   d.._"postgres_db"
#
#     print("Selecting rows from mobile table using cursor.fetchall")
#     cursor _ ?.c..
#     postgreSQL_s.._Query _ "s.. _ f.. mobile"
#
#     ?.e.. ?
#     mobile_records _ ?.f_m.. 2
#
#     print("Printing 2 rows")
#     ___ row __ ?
#         print("Id = " ? 0
#         print("Model = " ? 1
#         print("Price  = " ? 2 "\n")
#
#     mobile_records _ ?.f_m.. 2
#
#     print("Printing next 2 rows")
#     ___ row __ ?
#         print("Id = " ? 0
#         print("Model = " ? 1
#         print("Price  = " ? 2 "\n")
#
# ______ E.., ?.Er.. __ error
#     print("Error while fetching data from PostgreSQL" ?
#
# f__
#     # closing database connection.
#     __  c..
#         ?.c..
#         ?.c..
#         print("PostgreSQL connection is closed")
#
#
# # Output:
# #
# # Selecting rows from mobile table using cursor.fetchall
# #
# # Printing 2 rows
# #
# # Id =  1
# # Model =  IPhone XS
# # Price  =  1000.0
# #
# # Id =  2
# # Model =  Samsung Galaxy S9
# # Price  =  900.0
# #
# # Printing next 2 rows
# #
# # Id =  3
# # Model =  Google Pixel
# # Price  =  700.0
# #
# # Id =  4
# # Model =  LG
# # Price  =  800.0
# #
# # PostgreSQL connection is closed