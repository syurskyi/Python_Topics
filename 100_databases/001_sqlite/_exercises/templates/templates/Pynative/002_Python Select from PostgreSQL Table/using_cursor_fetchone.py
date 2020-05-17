_____ psycopg2

try:
   connection _ psycopg2.c..(user_"syurskyi",
                                  password_"1234",
                                  host_"127.0.0.1",
                                  port_"5432",
                                  database_"postgres_db")

   PostgreSQL_select_Query _ "select * from mobile"
   cursor _ connection.cursor()

   cursor.e..(PostgreSQL_select_Query)

   mobile_records_one _ cursor.fetchone()
   print ("Printing first record", mobile_records_one)

   mobile_records_two _ cursor.fetchone()
   print("Printing second record", mobile_records_two)

except (Exception, psycopg2.Error) as error :
    print ("Error while getting data from PostgreSQL", error)

finally:
    #closing database connection.
    __(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


# Output:
#
# Printing first record (1, 'IPhone XS', 1000.0)
# Printing second record (2, 'Samsung Galaxy S9', 900.0)
# PostgreSQL connection is closed

