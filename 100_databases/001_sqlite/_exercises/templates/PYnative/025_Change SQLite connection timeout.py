import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db', timeout=20)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT count(*) from SqliteDb_developers"""
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchone()
        print("Total rows are:  ", totalRows)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The Sqlite connection is closed")

readSqliteTable()


# Output:
#
# Connected to SQLite
# Total rows are:   (2,)
# The Sqlite connection is closed