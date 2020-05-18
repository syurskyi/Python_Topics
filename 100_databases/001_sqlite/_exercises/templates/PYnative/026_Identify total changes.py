_____ ?

___
    sqliteConnection _ ?.c..('SQLite_Python.db')
    cursor _ sqliteConnection.c..
    print("Connected to SQLite")

    sqlite_insert_query _ """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (4, 'Jos', 'jos@gmail.com', '2019-01-14', 9500);"""
    cursor.e..(sqlite_insert_query)

    sql_update_query _ """Update SqliteDb_developers set salary = 10000 where id = 4"""
    cursor.e..(sql_update_query)

    sql_delete_query _ """DELETE from SqliteDb_developers where id = 4"""
    cursor.e..(sql_delete_query)

    sqliteConnection.c..
    cursor.c..

_____ ?.E.. __ error:
    print("Error while working with SQLite", error)
f..
    __ (sqliteConnection):
        print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
        sqliteConnection.c..
        print("sqlite connection is closed")


# Output:
#
# Connected to SQLite
# Total Rows affected since the database connection was opened:  3
# sqlite connection is closed

