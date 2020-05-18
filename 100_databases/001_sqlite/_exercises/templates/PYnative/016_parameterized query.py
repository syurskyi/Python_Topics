_____ ?

___ deleteSqliteRecord(id):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")

        sql_update_query _ """DELETE from SqliteDb_developers where id = ?"""
        ?.e..(sql_update_query, (id, ))
        ?.c..
        print("Record deleted successfully")

        ?.c..

    _____ ?.E.. __ error:
        print("Failed to delete reocord from a sqlite table", error)
    f..
        __ (?):
            ?.c..
            print("sqlite connection is closed")

deleteSqliteRecord(5)


# Connected to SQLite
# Record deleted successfully
# sqlite connection is closed