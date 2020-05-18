_____ ?

def deleteRecord():
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        # Deleting single record now
        sql_delete_query _ """DELETE from SqliteDb_developers where id = 6"""
        cursor.e..(sql_delete_query)
        sqliteConnection.c..
        print("Record deleted successfully ")
        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to delete record from sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("the sqlite connection is closed")

deleteRecord()

# Connected to SQLite
# Record deleted successfully
# the sqlite connection is closed