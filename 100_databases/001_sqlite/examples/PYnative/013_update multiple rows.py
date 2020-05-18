import sqlite3

def updateMultipleRecords(recordList):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_update_query = """Update SqliteDb_developers set salary = ? where id = ?"""
        cursor.executemany(sqlite_update_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records updated successfully")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update multiple records of sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

records_to_update = [ (9700, 4), (7800, 5), (8400, 6) ]
updateMultipleRecords(records_to_update)


# Connected to SQLite
# Total 3 Records updated successfully
# The SQLite connection is closed

