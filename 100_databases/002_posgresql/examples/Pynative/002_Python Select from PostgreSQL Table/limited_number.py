import psycopg2

try:
    connection = psycopg2.connect(user="syurskyi",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

    print("Selecting rows from mobile table using cursor.fetchall")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from mobile"

    cursor.execute(postgreSQL_select_Query)
    mobile_records = cursor.fetchmany(2)

    print("Printing 2 rows")
    for row in mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")

    mobile_records = cursor.fetchmany(2)

    print("Printing next 2 rows")
    for row in mobile_records:
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