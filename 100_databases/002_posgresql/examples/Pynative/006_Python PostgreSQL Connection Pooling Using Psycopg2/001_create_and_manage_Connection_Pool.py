import psycopg2
from psycopg2 import pool
try:
    postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20,user = "syurskyi",
                                              password = "1234",
                                              host = "127.0.0.1",
                                              port = "5432",
                                              database = "postgres_db")
    if(postgreSQL_pool):
        print("Connection pool created successfully")

    # Use getconn() to Get Connection from connection pool
    ps_connection  = postgreSQL_pool.getconn()

    if(ps_connection):
        print("successfully recived connection from connection pool ")
        ps_cursor = ps_connection.cursor()
        ps_cursor.execute("select * from mobile")
        mobile_records = ps_cursor.fetchall()

        print ("Displaying rows from mobile table")
        for row in mobile_records:
            print (row)

        ps_cursor.close()

        #Use this method to release the connection object and send back to connection pool
        postgreSQL_pool.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
    # use closeall method to close all the active connection if you want to turn of the application
    if (postgreSQL_pool):
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