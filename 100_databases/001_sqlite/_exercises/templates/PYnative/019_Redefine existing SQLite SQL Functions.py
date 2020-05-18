_____ ?

def lower(string):
    return str(string).upper()

def getDeveloperName(id):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sqliteConnection.create_function("lower", 1, lower)
        select_query _ "SELECT lower(name) FROM SqliteDb_developers where id = ?"
        cursor.e..(select_query, (id,))
        name _ cursor.fetchone()
        print("Developer Name is", name)
        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to read data from sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("sqlite connection is closed")

getDeveloperName(1)

# Output:
#
# Connected to SQLite
# Developer Name is ('JAMES',)
# sqlite connection is closed
