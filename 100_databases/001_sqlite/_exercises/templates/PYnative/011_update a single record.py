_____ ?

def updateSqliteTable():
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")

        sql_update_query _ """Update SqliteDb_developers set salary = 10000 where id = 4"""
        ?.e..(sql_update_query)
        ?.c..
        print("Record Updated successfully ")
        ?.c..

    _____ ?.E.. __ error:
        print("Failed to update sqlite table", error)
    f..
        __ (?):
            ?.c..
            print("The SQLite connection is closed")

updateSqliteTable()


# Connected to SQLite
# Record Updated successfully
# The SQLite connection is closed