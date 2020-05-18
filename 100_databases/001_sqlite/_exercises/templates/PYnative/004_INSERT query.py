_____ ?

def insertVaribleIntoTable(id, name, email, joinDate, salary):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sqlite_insert_with_param _ """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple _ (id, name, email, joinDate, salary)
        cursor.e..(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to insert Python variable into sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("The SQLite connection is closed")

insertVaribleIntoTable(2, 'Joe', 'joe@pynative.com', '2019-05-19', 9000)
insertVaribleIntoTable(3, 'Ben', 'ben@pynative.com', '2019-02-23', 9500)


# onnected to SQLite
# Python Variables inserted successfully into SqliteDb_developers table
# sqlite connection is closed
# Connected to SQLite
# Python Variables inserted successfully into SqliteDb_developers table
# The SQLite connection is closed