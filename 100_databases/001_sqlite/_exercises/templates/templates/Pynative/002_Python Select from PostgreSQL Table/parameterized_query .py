_____ psycopg2

___ getMobileDetails(mobileID):
    ___
        connection _ psycopg2.c..(user_"syurskyi",
                                      password_"1234",
                                      host_"127.0.0.1",
                                      port_"5432",
                                      database_"postgres_db")

        print("Using Python variable in PostgreSQL select Query")
        cursor _ connection.c..
        postgreSQL_select_Query _ "select * from mobile where id = %s"

        cursor.e..(postgreSQL_select_Query, (mobileID,))
        mobile_records _ cursor.f_a..
        ___ row __ mobile_records:
            print("Id = ", row[0], )
            print("Model = ", row[1])
            print("Price  = ", row[2])

    ______ (E.., psycopg2.Error) __ error:
        print("Error fetching data from PostgreSQL table", error)

    f__
        # closing database connection
        __ (connection):
            cursor.c..
            connection.c..
            print("PostgreSQL connection is closed \n")

getMobileDetails(2)
getMobileDetails(3)


# Output:
#
# Using Python variable in PostgreSQL select Query
# Id =  2
# Model =  Samsung Galaxy S9
# Price  =  900.0
# PostgreSQL connection is closed
#
# Using Python variable in PostgreSQL select Query
# Id =  3
# Model =  Google Pixel
# Price  =  700.0
# PostgreSQL connection is closed