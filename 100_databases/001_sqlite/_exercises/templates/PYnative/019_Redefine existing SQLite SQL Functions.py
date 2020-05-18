import sqlite3

def lower(string):
    return str(string).upper()

def getDeveloperName(id):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqliteConnection.create_function("lower", 1, lower)
        select_query = "SELECT lower(name) FROM SqliteDb_developers where id = ?"
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

getDeveloperName(1)

# Output:
#
# Connected to SQLite
# Developer Name is ('JAMES',)
# sqlite connection is closed
