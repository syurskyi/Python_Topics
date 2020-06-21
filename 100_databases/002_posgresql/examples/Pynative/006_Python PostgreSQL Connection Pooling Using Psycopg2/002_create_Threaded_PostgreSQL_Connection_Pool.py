import psycopg2
from psycopg2 import pool
try:
    threaded_postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(5, 20,user = "postgres",
                                              password = "pass@#29",
                                              host = "127.0.0.1",
                                              port = "5432",
                                              database = "postgres_db")
    if(threaded_postgreSQL_pool):
        print("Connection pool created successfully using ThreadedConnectionPool")


    # Use getconn() method to Get Connection from connection pool
    ps_connection  = threaded_postgreSQL_pool.getconn()

    if(ps_connection):

        print("successfully recived connection from connection pool ")
        ps_cursor = ps_connection.cursor()
        ps_cursor.execute("select * from mobile")
        mobile_records = ps_cursor.fetchmany(2)

        print ("Displaying rows from mobile table")
        for row in mobile_records:
            print (row)

        ps_cursor.close()

        #Use this method to release the connection object and send back ti connection pool
        threaded_postgreSQL_pool.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
    # use closeall method to close all the active connection if you want to turn of the application
    if (threaded_postgreSQL_pool):
        threaded_postgreSQL_pool.closeall
    print("Threaded PostgreSQL connection pool is closed")



# Connection pool created successfully using ThreadedConnectionPool
# successfully recived connection from connection pool
# Displaying rows from mobile table
# (4, 'LG V30', 800.0)
# (5, 'iPhone 8 Plus', 750.0)
# Put away a PostgreSQL connection
# Threaded PostgreSQL connection pool is closed