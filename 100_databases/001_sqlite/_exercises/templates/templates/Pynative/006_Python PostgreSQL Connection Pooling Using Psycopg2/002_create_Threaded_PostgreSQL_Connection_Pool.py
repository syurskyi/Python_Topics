_____ ?
____ ? _____ pool
___
    threaded_postgreSQL_pool _ ?.pool.ThreadedConnectionPool(5, 20,u.. _ "postgres",
                                              p.. _ "pass@#29",
                                              h.. _ "127.0.0.1",
                                              p.. _ "5432",
                                              d.. _ "postgres_db")
    __(threaded_postgreSQL_pool):
        print("Connection pool created successfully using ThreadedConnectionPool")


    # Use getconn() method to Get Connection from connection pool
    ps_connection  _ threaded_postgreSQL_pool.getconn()

    __(ps_connection):

        print("successfully recived connection from connection pool ")
        ps_cursor _ ps_connection.c..
        ps_cursor.e..("s.. * from mobile")
        mobile_records _ ps_cursor.f_m..(2)

        print ("Displaying rows from mobile table")
        ___ row __ mobile_records:
            print (row)

        ps_cursor.c..

        #Use this method to release the connection object and send back ti connection pool
        threaded_postgreSQL_pool.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

______ (E.., ?.DE..) __ error :
    print ("Error while connecting to PostgreSQL", error)

f__
    #closing database connection.
    # use closeall method to close all the active connection if you want to turn of the application
    __ (threaded_postgreSQL_pool):
        threaded_postgreSQL_pool.closeall
    print("Threaded PostgreSQL connection pool is closed")



# Connection pool created successfully using ThreadedConnectionPool
# successfully recived connection from connection pool
# Displaying rows from mobile table
# (4, 'LG V30', 800.0)
# (5, 'iPhone 8 Plus', 750.0)
# Put away a PostgreSQL connection
# Threaded PostgreSQL connection pool is closed