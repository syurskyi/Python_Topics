_____ ?

___ updateSqliteTable(id, salary):
    ___
        ? _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")

        sql_update_query _ """Update SqliteDb_developers set salary = ? w.. id = ?"""
        data _ (salary, id)
        ?.e..(sql_update_query, data)
        ?.c..
        print("Record Updated successfully")
        ?.c..

    _____ ?.E.. __ error:
        print("Failed to update sqlite table", error)
    f..
        __ (?):
            ?.c..
            print("The sqlite connection is closed")

updateSqliteTable(3, 7500)


# Connected to SQLite
# Record Updated successfully
# The sqlite connection is closed