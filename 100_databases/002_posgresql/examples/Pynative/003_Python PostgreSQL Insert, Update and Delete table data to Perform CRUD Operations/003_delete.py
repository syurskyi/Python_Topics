import psycopg2


def deleteData(mobileId):
    try:
        connection = psycopg2.connect(user="syurskyi",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")

        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = """Delete from mobile where id = %s"""
        cursor.execute(sql_delete_query, (mobileId, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

id4 = 4
id5 = 5
deleteData(id4)
deleteData(id5)


# 1 Record deleted successfully
# PostgreSQL connection is closed
#
# 1 Record deleted successfully
# PostgreSQL connection is closed

