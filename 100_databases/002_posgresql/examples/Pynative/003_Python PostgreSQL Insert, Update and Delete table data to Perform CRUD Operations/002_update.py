import psycopg2

def updateTable(mobileId, price):
    try:
        connection = psycopg2.connect(user="syurskyi",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (mobileId, ))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update mobile set price = %s where id = %s"""
        cursor.execute(sql_update_query, (price, mobileId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (mobileId,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

id = 3
price = 970
updateTable(id, price)