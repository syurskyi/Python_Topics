_____ ?
____ ? _____ pool
___
    postgreSQL_pool _ ?.pool.SimpleConnectionPool(1, 20,u.. _ "syurskyi",
                                              p.. _ "1234",
                                              h.. _ "127.0.0.1",
                                              p.. _ "5432",
                                              d.. _ "postgres_db")
    __(postgreSQL_pool):
        print("Connection pool created successfully")

    # Use getconn() to Get Connection from connection pool
    ps_connection  _ postgreSQL_pool.getconn()

    __(ps_connection):
        print("successfully recived connection from connection pool ")
        ps_cursor _ ps_connection.c..
        ps_cursor.e..("s.. _ from mobile")
        mobile_records _ ps_cursor.f_a..

        print ("Displaying rows from mobile table")
        ___ row __ mobile_records:
            print (row)

        ps_cursor.c..

        #Use this method to release the connection object and send back to connection pool
        postgreSQL_pool.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

______ (E.., ?.DE..) __ error :
    print ("Error while connecting to PostgreSQL", error)

f__
    #closing database connection.
    # use closeall method to close all the active connection if you want to turn of the application
    __ (postgreSQL_pool):
        postgreSQL_pool.closeall
    print("PostgreSQL connection pool is closed")


# ou should get the following output:
#
# Connection pool created successfully
# successfully recived connection from connection pool
# Displaying rows from mobile table
# (4, 'LG V30', 800.0)
# (5, 'iPhone 8 Plus', 750.0)
# (3, 'Samsung Galaxy S9', 850.0)
# (1, 'IPhone X', 1000.0)
# Put away a PostgreSQL connection
# PostgreSQL connection pool is closed