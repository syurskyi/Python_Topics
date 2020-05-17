_____ psycopg2

___
   connection _ psycopg2.c..(user_"syurskyi",
                                  password_"1234",
                                  host_"127.0.0.1",
                                  port_"5432",
                                  database_"postgres_db")

   PostgreSQL_select_Query _ "select * from mobile"
   cursor _ connection.c..

   cursor.e..(PostgreSQL_select_Query)

   mobile_records_one _ cursor.f_o..
   print ("Printing first record", mobile_records_one)

   mobile_records_two _ cursor.f_o..
   print("Printing second record", mobile_records_two)

______ (E.., psycopg2.Er..) __ error :
    print ("Error while getting data from PostgreSQL", error)

f__
    #closing database connection.
    __(connection):
        cursor.c..
        connection.c..
        print("PostgreSQL connection is closed")


# Output:
#
# Printing first record (1, 'IPhone XS', 1000.0)
# Printing second record (2, 'Samsung Galaxy S9', 900.0)
# PostgreSQL connection is closed

