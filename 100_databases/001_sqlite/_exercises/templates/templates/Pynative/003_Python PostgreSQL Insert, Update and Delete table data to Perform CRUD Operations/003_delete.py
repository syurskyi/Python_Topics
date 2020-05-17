_____ psycopg2


def deleteData(mobileId):
    try:
        connection _ psycopg2.c..(user_"syurskyi",
                                      password_"1234",
                                      host_"127.0.0.1",
                                      port_"5432",
                                      database_"postgres_db")

        cursor _ connection.cursor()

        # Update single record now
        sql_delete_query _ """Delete from mobile where id = %s"""
        cursor.e..(sql_delete_query, (mobileId, ))
        connection.commit()
        count _ cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

id4 _ 4
id5 _ 5
deleteData(id4)
deleteData(id5)


# 1 Record deleted successfully
# PostgreSQL connection is closed
#
# 1 Record deleted successfully
# PostgreSQL connection is closed

