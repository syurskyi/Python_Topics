import psycopg2

def getMobileDetails(mobileID):
    try:
        connection = psycopg2.connect(user="syurskyi",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")

        print("Using Python variable in PostgreSQL select Query")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from mobile where id = %s"

        cursor.execute(postgreSQL_select_Query, (mobileID,))
        mobile_records = cursor.fetchall()
        for row in mobile_records:
            print("Id = ", row[0], )
            print("Model = ", row[1])
            print("Price  = ", row[2])

    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL table", error)

    finally:
        # closing database connection
        if (connection):
            cursor.close()
            connection.close()
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