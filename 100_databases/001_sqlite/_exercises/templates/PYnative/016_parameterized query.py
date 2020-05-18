_____ ?

def deleteSqliteRecord(id):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sql_update_query _ """DELETE from SqliteDb_developers where id = ?"""
        cursor.e..(sql_update_query, (id, ))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to delete reocord from a sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("sqlite connection is closed")

deleteSqliteRecord(5)


# Connected to SQLite
# Record deleted successfully
# sqlite connection is closed