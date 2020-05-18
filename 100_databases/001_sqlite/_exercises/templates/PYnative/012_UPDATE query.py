_____ ?

def updateSqliteTable(id, salary):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sql_update_query _ """Update SqliteDb_developers set salary = ? where id = ?"""
        data _ (salary, id)
        cursor.e..(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to update sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("The sqlite connection is closed")

updateSqliteTable(3, 7500)


# Connected to SQLite
# Record Updated successfully
# The sqlite connection is closed