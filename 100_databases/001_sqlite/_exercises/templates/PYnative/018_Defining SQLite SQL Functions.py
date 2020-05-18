import sqlite3

def _toTileCase(string):
    return str(string).title()

def getDeveloperName(id):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqliteConnection.create_function("TOTILECASE", 1, _toTileCase)
        select_query = "SELECT TOTILECASE(name) FROM SqliteDb_developers where id = ?"
        cursor.execute(select_query, (id,))
        name = cursor.fetchone()
        print("Developer Name is", name)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

getDeveloperName(2)

# Output:
#
# Connected to SQLite
# Developer Name is ('Joe',)
# sqlite connection is closed