_____ psycopg2

def updateInBulk(records):
    ___
        ps_connection _ psycopg2.c..(user_"syurskyi",
                                         password_"1234",
                                         host_"127.0.0.1",
                                         port_"5432",
                                         database_"postgres_db")
        cursor _ ps_connection.c..

        # Update multiple records
        sql_update_query _ """Update mobile set price = %s where id = %s"""
        cursor.executemany(sql_update_query, records)
        ps_connection.c..

        row_count _ cursor.rowcount
        print(row_count, "Records Updated")

    ______ (E.., psycopg2.Error) __ error:
        print("Error while updating PostgreSQL table", error)

    f__
        # closing database connection.
        __ (ps_connection):
            cursor.c..
            ps_connection.c..
            print("PostgreSQL connection is closed")

tuples _ [(750, 4), (950, 5)]
updateInBulk(tuples)


# Output:
#
# 2 Records Updated
# PostgreSQL connection is closed