import sqlite3

def deleteSqliteRecord(id):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """DELETE from SqliteDb_developers where id = ?"""
        cursor.execute(sql_update_query, (id, ))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

deleteSqliteRecord(5)


# Connected to SQLite
# Record deleted successfully
# sqlite connection is closed