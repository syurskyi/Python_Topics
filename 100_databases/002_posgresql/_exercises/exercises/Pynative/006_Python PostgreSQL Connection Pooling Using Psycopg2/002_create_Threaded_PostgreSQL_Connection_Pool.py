# _____ ?
# ____ ? _____ pool
# ___
#     threaded_postgreSQL_pool _ ?.p__.TCP.. 5 20,u.. _ "postgres"
#                                               p.. _ "pass@#29"
#                                               h.. _ "127.0.0.1"
#                                               p.. _ "5432"
#                                               d.. _ "postgres_db"
#     __ ?
#         print("Connection pool created successfully using ThreadedConnectionPool")
#
#
#     # Use getconn() method to Get Connection from connection pool
#     ps_connection  _ ?.g..
#
#     __ ?
#
#         print("successfully recived connection from connection pool ")
#         ps_cursor _ ?.c.
#         ?.e.. "s.. _ f.. mobile"
#         mobile_records _ ?.f_m.. 2
#
#         print ("Displaying rows f.. mobile table")
#         ___ row __ ?
#             print ?
#
#         ?.c..
#
#         #Use this method to release the connection object and send back ti connection pool
#         ?.p.. p_c..
#         print("Put away a PostgreSQL connection")
#
# ______ E.. ?.DE.. __ error
#     print ("Error while connecting to PostgreSQL" ?
#
# f__
#     #closing database connection.
#     # use closeall method to close all the active connection if you want to turn of the application
#     __ ?
#         ?.c_a..
#     print("Threaded PostgreSQL connection pool is closed")
#
#
#
# # Connection pool created successfully using ThreadedConnectionPool
# # successfully recived connection from connection pool
# # Displaying rows from mobile table
# # (4, 'LG V30', 800.0)
# # (5, 'iPhone 8 Plus', 750.0)
# # Put away a PostgreSQL connection
# # Threaded PostgreSQL connection pool is closed