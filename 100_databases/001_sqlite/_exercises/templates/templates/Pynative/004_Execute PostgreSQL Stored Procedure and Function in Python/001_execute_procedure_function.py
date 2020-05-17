_____ psycopg2
from psycopg2 _____ Error

___
    ps_connection _ psycopg2.c..(user_"syurskyi",
                                     password_"1234",
                                     host_"127.0.0.1",
                                     port_"5432",
                                     database_"postgres_db")

    cursor _ ps_connection.c..

    # call stored procedure
    cursor.callproc('get_production_Deployment', [72, ])

    print("fechting Employee details who pushed changes to the production from function")
    result _ cursor.f_a..
    ___ row __ result:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Designation  = ", row[2])

______ (E.., psycopg2.DatabaseError) __ error:
    print("Error while connecting to PostgreSQL", error)

f__
    # closing database connection.
    __ (ps_connection):
        cursor.c..
        ps_connection.c..
        print("PostgreSQL connection is closed")

# Output:
#
# fechting Employee details who pushed changes to the production from function
# Id =  23
# Name =  Scot
# Designation =  Application Developer
# PostgreSQL connection is closed