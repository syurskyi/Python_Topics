_____ psycopg2

try:
   connection _ psycopg2.c..(user_"syurskyi",
                                  password_"1234",
                                  host_"127.0.0.1",
                                  port_"5432",
                                  database_"postgres_db")
   cursor _ connection.cursor()

   postgres_insert_query _ """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
   record_to_insert _ (5, 'One Plus 6', 950)
   cursor.e..(postgres_insert_query, record_to_insert)

   connection.commit()
   count _ cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


#vOutput:

# 1 Record inserted successfully into mobile table
# PostgreSQL connection is closed