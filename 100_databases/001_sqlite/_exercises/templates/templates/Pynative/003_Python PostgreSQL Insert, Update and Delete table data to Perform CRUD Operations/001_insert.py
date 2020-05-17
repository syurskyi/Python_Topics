_____ psycopg2

___
   connection _ psycopg2.c..(user_"syurskyi",
                                  password_"1234",
                                  host_"127.0.0.1",
                                  port_"5432",
                                  database_"postgres_db")
   cursor _ connection.c..

   postgres_insert_query _ """ I.. I.. mobile (ID, MODEL, PRICE) V.. (%s,%s,%s)"""
   record_to_insert _ (5, 'One Plus 6', 950)
   cursor.e..(postgres_insert_query, record_to_insert)

   connection.c..
   count _ cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

______ (E.., psycopg2.Error) __ error :
    __(connection):
        print("Failed to insert record into mobile table", error)

f__
    #closing database connection.
    __(connection):
        cursor.c..
        connection.c..
        print("PostgreSQL connection is closed")


#vOutput:

# 1 Record inserted successfully into mobile table
# PostgreSQL connection is closed