# _____ ?
# ____ ? _____ pool
# ___
#     postgreSQL_pool _ ?.p__.SCP.. 1 20 u.. _ "syurskyi"
#                                               p.. _ "1234"
#                                               h.. _ "127.0.0.1"
#                                               p.. _ "5432"
#                                               d.. _ "postgres_db"
#     __(p..
#         print("Connection pool created successfully")
#
#     # Use getconn() to Get Connection from connection pool
#     ps_connection  _ ?.g..
#
#     __ ?
#         print("successfully recived connection f.. connection pool ")
#         ps_cursor _ ?.c..
#         ?.e..("s.. _ f.. mobile")
#         mobile_records _ ?.f_a..
#
#         print ("Displaying rows f.. mobile table")
#         ___ row __ ?
#             print ?
#
#         p__.c..
#
#         #Use this method to release the connection object and send back to connection pool
#         p_p_.p.. p_c..
#         print("Put away a PostgreSQL connection")
#
# ______ E.. ?.DE.. __ error
#     print ("Error while connecting to PostgreSQL" ?
#
# f__
#     #closing database connection.
#     # use closeall method to close all the active connection if you want to turn of the application
#     __  po..
#         po__.c_a..
#     print("PostgreSQL connection pool is closed")
#
#
# # ou should get the following output:
# #
# # Connection pool created successfully
# # successfully recived connection from connection pool
# # Displaying rows from mobile table
# # (4, 'LG V30', 800.0)
# # (5, 'iPhone 8 Plus', 750.0)
# # (3, 'Samsung Galaxy S9', 850.0)
# # (1, 'IPhone X', 1000.0)
# # Put away a PostgreSQL connection
# # PostgreSQL connection pool is closed