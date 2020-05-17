_____ psycopg2

try:
    connection _ psycopg2.c..(user_"syurskyi",
                                  password_"1234",
                                  host_"127.0.0.1",
                                  port_"5432",
                                  database_"postgres_db")

    print("Selecting rows from mobile table using cursor.fetchall")
    cursor _ connection.cursor()
    postgreSQL_select_Query _ "select * from mobile"

    cursor.e..(postgreSQL_select_Query)
    mobile_records _ cursor.fetchmany(2)

    print("Printing 2 rows")
    ___ row __ mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")

    mobile_records _ cursor.fetchmany(2)

    print("Printing next 2 rows")
    ___ row __ mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


# Output:
#
# Selecting rows from mobile table using cursor.fetchall
#
# Printing 2 rows
#
# Id =  1
# Model =  IPhone XS
# Price  =  1000.0
#
# Id =  2
# Model =  Samsung Galaxy S9
# Price  =  900.0
#
# Printing next 2 rows
#
# Id =  3
# Model =  Google Pixel
# Price  =  700.0
#
# Id =  4
# Model =  LG
# Price  =  800.0
#
# PostgreSQL connection is closed