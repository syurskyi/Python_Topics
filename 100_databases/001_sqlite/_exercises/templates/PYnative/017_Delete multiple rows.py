import sqlite3

def deleteMultipleRecords(idList):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_update_query = """DELETE from SqliteDb_developers where id = ?"""

        cursor.executemany(sqlite_update_query, idList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records deleted successfully")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete multiple records from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

idsToDelete = [(4,),(3,)]
deleteMultipleRecords(idsToDelete)