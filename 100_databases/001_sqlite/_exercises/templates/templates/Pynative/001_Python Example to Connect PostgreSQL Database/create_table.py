_____ psycopg2
from psycopg2 _____ Error

try:
    connection _ psycopg2.c..(user_"syurskyi",
                                  password_"1234",
                                  host_"127.0.0.1",
                                  port_"5432",
                                  database_"postgres_db")

    cursor _ connection.c..

    create_table_query _ '''C.. T.. mobile
          (ID INT P.. K..     NOT NULL,
          MODEL           T...    NOT NULL,
          PRICE         REAL); '''

    cursor.e..(create_table_query)
    connection.c..
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)
finally:
    # closing database connection.
    __ (connection):
        cursor.c..
        connection.c..
        print("PostgreSQL connection is closed")