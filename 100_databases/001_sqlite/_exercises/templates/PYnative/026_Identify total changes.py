_____ ?

___
    sqliteConnection _ ?.c..('SQLite_Python.db')
    cursor _ ?.c..
    print("Connected to SQLite")

    sqlite_insert_query _ """I.. I.. SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          V.. (4, 'Jos', 'jos@gmail.com', '2019-01-14', 9500);"""
    ?.e..(sqlite_insert_query)

    sql_update_query _ """Update SqliteDb_developers set salary = 10000 where id = 4"""
    ?.e..(sql_update_query)

    sql_delete_query _ """DELETE from SqliteDb_developers where id = 4"""
    ?.e..(sql_delete_query)

    ?.c..
    ?.c..

_____ ?.E.. __ error:
    print("Error while working with SQLite", error)
f..
    __ (?):
        print("Total Rows affected since the database connection was opened: ", ?.total_changes)
        ?.c..
        print("sqlite connection is closed")


# Output:
#
# Connected to SQLite
# Total Rows affected since the database connection was opened:  3
# sqlite connection is closed

