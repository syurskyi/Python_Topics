_____ psycopg2

___ updateTable(mobileId, price):
    ___
        connection _ psycopg2.c..(user_"syurskyi",
                                      password_"1234",
                                      host_"127.0.0.1",
                                      port_"5432",
                                      database_"postgres_db")

        cursor _ connection.c..

        print("Table Before updating record ")
        sql_select_query _ """select * from mobile w.. id = %s"""
        cursor.e..(sql_select_query, (mobileId, ))
        record _ cursor.f_o..
        print(record)

        # Update single record now
        sql_update_query _ """Update mobile set price = %s w.. id = %s"""
        cursor.e..(sql_update_query, (price, mobileId))
        connection.c..
        count _ cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query _ """select * from mobile w.. id = %s"""
        cursor.e..(sql_select_query, (mobileId,))
        record _ cursor.f_o..
        print(record)

    ______ (E.., psycopg2.Er..) __ error:
        print("Error in update operation", error)

    f__
        # closing database connection.
        __ (connection):
            cursor.c..
            connection.c..
            print("PostgreSQL connection is closed")

id _ 3
price _ 970
updateTable(id, price)