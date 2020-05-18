_____ ?

___ lower(string):
    return str(string).upper()

___ getDeveloperName(id):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")

        ?.create_function("lower", 1, lower)
        select_query _ "S.. lower(name) FROM SqliteDb_developers w.. id = ?"
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

getDeveloperName(1)

# Output:
#
# Connected to SQLite
# Developer Name is ('JAMES',)
# sqlite connection is closed
