_____ ?

def updateMultipleRecords(recordList):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sqlite_update_query _ """Update SqliteDb_developers set salary = ? where id = ?"""
        cursor.executemany(sqlite_update_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records updated successfully")
        sqliteConnection.commit()
        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to update multiple records of sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("The SQLite connection is closed")

records_to_update _ [ (9700, 4), (7800, 5), (8400, 6) ]
updateMultipleRecords(records_to_update)


# Connected to SQLite
# Total 3 Records updated successfully
# The SQLite connection is closed

