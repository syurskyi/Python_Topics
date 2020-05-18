_____ ?

___
   connection _ ?.c..(u.._"syurskyi",
                                  p.._"1234",
                                  h.._"127.0.0.1",
                                  p.._"5432",
                                  d.._"postgres_db")
   cursor _ connection.c..

   postgres_insert_query _ """ I.. I.. mobile (ID, MODEL, PRICE) V.. (%s,%s,%s)"""
   record_to_insert _ (5, 'One Plus 6', 950)
   cursor.e..(postgres_insert_query, record_to_insert)

   connection.c..
   count _ cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

______ (E.., ?.Er..) __ error :
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