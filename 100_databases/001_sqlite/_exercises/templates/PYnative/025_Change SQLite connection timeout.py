_____ ?

___ readSqliteTable
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db', timeout_20)
        cursor _ ?.c..
        print("Connected to SQLite")

        sqlite_select_query _ """S.. count(_) f.. SqliteDb_developers"""
        ?.e..(sqlite_select_query)
        totalRows _ ?.f_o..
        print("Total rows are:  ", totalRows)
        ?.c..

    _____ ?.E.. __ error:
        print("Failed to read data from sqlite table" ?
    f..
        __ (?
            ?.c..
            print("The Sqlite connection is closed")

readSqliteTable()


# Output:
#
# Connected to SQLite
# Total rows are:   (2,)
# The Sqlite connection is closed