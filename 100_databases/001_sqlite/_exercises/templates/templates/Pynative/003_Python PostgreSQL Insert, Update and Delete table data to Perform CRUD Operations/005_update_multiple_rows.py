_____ psycopg2

def updateInBulk(records):
    try:
        ps_connection _ psycopg2.c..(user_"syurskyi",
                                         password_"1234",
                                         host_"127.0.0.1",
                                         port_"5432",
                                         database_"postgres_db")
        cursor _ ps_connection.cursor()

        # Update multiple records
        sql_update_query _ """Update mobile set price = %s where id = %s"""
        cursor.executemany(sql_update_query, records)
        ps_connection.commit()

        row_count _ cursor.rowcount
        print(row_count, "Records Updated")

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")

tuples _ [(750, 4), (950, 5)]
updateInBulk(tuples)


# Output:
#
# 2 Records Updated
# PostgreSQL connection is closed