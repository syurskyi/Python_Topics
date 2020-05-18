_____ ?

___
    sqliteConnection _ ?.c..('SQLite_Python.db')
    cursor _ sqliteConnection.c..
    print("Successfully Connected to SQLite")

    sqlite_insert_query _ """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                           VALUES 
                          (1,'James','james@pynative.com','2019-03-17',8000)"""

    count _ cursor.e..(sqlite_insert_query)
    sqliteConnection.c..
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.c..

_____ ?.E.. __ error:
    print("Failed to insert data into sqlite table", error)
f..
    __ (sqliteConnection):
        sqliteConnection.c..
        print("The SQLite connection is closed")

# Successfully Connected to SQLite
# Record inserted successfully into SqliteDb_developers table
# The SQLite connection is closed