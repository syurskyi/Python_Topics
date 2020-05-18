_____ ?

___ updateMultipleRecords(recordList):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")

        sqlite_update_query _ """Update SqliteDb_developers set salary = ? where id = ?"""
        ?.e_m..(sqlite_update_query, recordList)
        ?.c..
        print("Total", ?.r.., "Records updated successfully")
        ?.c..
        ?.c..

    _____ ?.E.. __ error:
        print("Failed to update multiple records of sqlite table", error)
    f..
        __ (?):
            ?.c..
            print("The SQLite connection is closed")

records_to_update _ [ (9700, 4), (7800, 5), (8400, 6) ]
updateMultipleRecords(records_to_update)


# Connected to SQLite
# Total 3 Records updated successfully
# The SQLite connection is closed

