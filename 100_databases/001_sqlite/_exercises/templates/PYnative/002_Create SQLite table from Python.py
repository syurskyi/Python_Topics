_____ ?

___
    sqliteConnection _ ?.c..('SQLite_Python.db')
    sqlite_create_table_query _ '''CREATE TABLE SqliteDb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''

    cursor _ sqliteConnection.c..
    print("Successfully Connected to SQLite")
    cursor.e..(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.c..

_____ ?.E.. __ error:
    print("Error while creating a sqlite table", error)
f..
    __ (sqliteConnection):
        sqliteConnection.c..
        print("sqlite connection is closed")


# Successfully Connected to SQLite
# SQLite table created:
# the sqlite connection is closed