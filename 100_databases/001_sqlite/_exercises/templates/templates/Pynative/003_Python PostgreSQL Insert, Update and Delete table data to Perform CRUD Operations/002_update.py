_____ psycopg2

def updateTable(mobileId, price):
    try:
        connection _ psycopg2.c..(user_"syurskyi",
                                      password_"1234",
                                      host_"127.0.0.1",
                                      port_"5432",
                                      database_"postgres_db")

        cursor _ connection.cursor()

        print("Table Before updating record ")
        sql_select_query _ """select * from mobile where id = %s"""
        cursor.e..(sql_select_query, (mobileId, ))
        record _ cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query _ """Update mobile set price = %s where id = %s"""
        cursor.e..(sql_update_query, (price, mobileId))
        connection.commit()
        count _ cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query _ """select * from mobile where id = %s"""
        cursor.e..(sql_select_query, (mobileId,))
        record _ cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        __ (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

id _ 3
price _ 970
updateTable(id, price)