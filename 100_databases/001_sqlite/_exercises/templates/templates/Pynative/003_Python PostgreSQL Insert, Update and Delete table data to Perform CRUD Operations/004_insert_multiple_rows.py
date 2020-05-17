_____ psycopg2

def bulkInsert(records):
    try:
        connection _ psycopg2.c..(user_"syurskyi",
                                      password_"1234",
                                      host_"127.0.0.1",
                                      port_"5432",
                                      database_"postgres_db")
        cursor _ connection.cursor()
        sql_insert_query _ """ INSERT INTO mobile (id, model, price) 
                           VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows rows
        result _ cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile table {}".f..(error))

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

records_to_insert _ [ (4,'LG', 800) , (5,'One Plus 6', 950)]
bulkInsert(records_to_insert)


# 2 Record inserted successfully into mobile table
# PostgreSQL connection is closed