_____ ?
____ ? _____ Er..

___
    connection _ ?.c..(user_"syurskyi",
                                  password_"1234",
                                  host_"127.0.0.1",
                                  port_"5432",
                                  database_"postgres_db")

    cursor _ connection.c..

    create_table_query _ '''C.. T.. mobile
          (ID IN. P.. K..     N.. N..,
          MODEL           T...    N.. N..,
          PRICE         RE.); '''

    cursor.e..(create_table_query)
    connection.c..
    print("Table created successfully in PostgreSQL ")

______ (E.., ?.DE..) __ error:
    print("Error while creating PostgreSQL table", error)
f__
    # closing database connection.
    __ (connection):
        cursor.c..
        connection.c..
        print("PostgreSQL connection is closed")