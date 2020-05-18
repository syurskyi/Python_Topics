_____ ?

___ deleteMultipleRecords(idList):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")
        sqlite_update_query _ """DELETE f.. SqliteDb_developers w.. id = ?"""

        ?.e_m..(sqlite_update_query, idList)
        ?.c..
        print("Total", ?.r.., "Records deleted successfully")
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