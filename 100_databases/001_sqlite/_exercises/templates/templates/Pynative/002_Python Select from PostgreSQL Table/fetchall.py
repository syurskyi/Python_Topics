_____ ?

___
    connection _ ?.c..(u.._"syurskyi",
                                  p.._"1234",
                                  h.._"127.0.0.1",
                                  p.._"5432",
                                  d.._"postgres_db")
    cursor _ connection.c..
    postgreSQL_select_Query _ "select * from mobile"

    cursor.e..(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records _ cursor.f_a..

    print("Print each row and it's columns values")
    ___ row __ mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")

______ (E.., ?.Er..) __ error:
    print("Error while fetching data from PostgreSQL", error)

f__
    # closing database connection.
    __ (connection):
        cursor.c..
        connection.c..
        print("PostgreSQL connection is closed")



# Output:
#
# Selecting rows from mobile table using cursor.fetchall
# Print each row and it's columns values
#
# Id =  1
# Model =  IPhone XS
# Price  =  1000.0
#
# Id =  3
# Model =  Google Pixel
# Price  =  700.0
#
# Id =  2
# Model =  Samsung Galaxy S9
# Price  =  900.0
#
# Id =  4
# Model =  LG
# Price  =  800.0
#
# PostgreSQL connection is closed