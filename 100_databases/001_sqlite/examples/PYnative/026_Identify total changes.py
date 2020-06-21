import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_insert_query = """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (4, 'Jos', 'jos@gmail.com', '2019-01-14', 9500);"""
    cursor.execute(sqlite_insert_query)

    sql_update_query = """Update SqliteDb_developers set salary = 10000 where id = 4"""
    cursor.execute(sql_update_query)

    sql_delete_query = """DELETE from SqliteDb_developers where id = 4"""
    cursor.execute(sql_delete_query)

    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error while working with SQLite", error)
finally:
    if (sqliteConnection):
        print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
        sqliteConnection.close()
        print("sqlite connection is closed")


# Output:
#
# Connected to SQLite
# Total Rows affected since the database connection was opened:  3
# sqlite connection is closed

