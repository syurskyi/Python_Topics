_____ ?

___
   connection _ ?.c..(u.._"syurskyi",
                                  p.._"1234",
                                  h.._"127.0.0.1",
                                  p.._"5432",
                                  d.._"postgres_db")

   PostgreSQL_select_Query _ "select * from mobile"
   cursor _ connection.c..

   cursor.e..(PostgreSQL_select_Query)

   mobile_records_one _ cursor.f_o..
   print ("Printing first record", mobile_records_one)

   mobile_records_two _ cursor.f_o..
   print("Printing second record", mobile_records_two)

______ (E.., ?.Er..) __ error :
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

