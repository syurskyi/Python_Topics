import psycopg2

try:
   connection = psycopg2.connect(user="syurskyi",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

   PostgreSQL_select_Query = "select * from mobile"
   cursor = connection.cursor()

   cursor.execute(PostgreSQL_select_Query)

   mobile_records_one = cursor.fetchone()
   print ("Printing first record", mobile_records_one)

   mobile_records_two = cursor.fetchone()
   print("Printing second record", mobile_records_two)

except (Exception, psycopg2.Error) as error :
    print ("Error while getting data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


# Output:
#
# Printing first record (1, 'IPhone XS', 1000.0)
# Printing second record (2, 'Samsung Galaxy S9', 900.0)
# PostgreSQL connection is closed

