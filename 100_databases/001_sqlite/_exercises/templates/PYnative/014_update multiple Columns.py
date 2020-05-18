_____ ?

def updateMultipleColumns(id, salary, email):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sqlite_update_query _ """Update new_developers set salary = ?, email = ? where id = ?"""
        columnValues _ (salary, email, id)
        cursor.e..(sqlite_update_query, columnValues)
        sqliteConnection.c..
        print("Multiple columns updated successfully")
        sqliteConnection.c..
        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to update multiple columns of sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("sqlite connection is closed")

updateMultipleColumns(3, 6500, 'ben_stokes@gmail.com')


# Connected to SQLite
# Multiple columns updated successfully
# sqlite connection is closed

