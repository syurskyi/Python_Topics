_____ ?

def deleteMultipleRecords(idList):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")
        sqlite_update_query _ """DELETE from SqliteDb_developers where id = ?"""

        ?.executemany(sqlite_update_query, idList)
        ?.c..
        print("Total", ?.rowcount, "Records deleted successfully")
        ?.c..
        ?.c..

    _____ ?.E.. __ error:
        print("Failed to delete multiple records from sqlite table", error)
    f..
        __ (?):
            ?.c..
            print("sqlite connection is closed")

idsToDelete _ [(4,),(3,)]
deleteMultipleRecords(idsToDelete)