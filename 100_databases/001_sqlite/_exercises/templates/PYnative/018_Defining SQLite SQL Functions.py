_____ ?

def _toTileCase(string):
    return str(string).title()

def getDeveloperName(id):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")

        ?.create_function("TOTILECASE", 1, _toTileCase)
        select_query _ "SELECT TOTILECASE(name) FROM SqliteDb_developers where id = ?"
        ?.e..(select_query, (id,))
        name _ ?.fetchone()
        print("Developer Name is", name)
        ?.c..

    _____ ?.E.. __ error:
        print("Failed to read data from sqlite table", error)
    f..
        __ (?):
            ?.c..
            print("sqlite connection is closed")

getDeveloperName(2)

# Output:
#
# Connected to SQLite
# Developer Name is ('Joe',)
# sqlite connection is closed