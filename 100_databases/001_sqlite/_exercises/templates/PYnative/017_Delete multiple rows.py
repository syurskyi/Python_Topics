_____ ?

def deleteMultipleRecords(idList):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")
        sqlite_update_query _ """DELETE from SqliteDb_developers where id = ?"""

        cursor.executemany(sqlite_update_query, idList)
        sqliteConnection.c..
        print("Total", cursor.rowcount, "Records deleted successfully")
        sqliteConnection.c..
        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to delete multiple records from sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("sqlite connection is closed")

idsToDelete _ [(4,),(3,)]
deleteMultipleRecords(idsToDelete)