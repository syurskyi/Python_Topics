_____ ?

def insertMultipleRecords(recordList):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sqlite_insert_query _ """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (?, ?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.c..
        print("Total", cursor.rowcount, "Records inserted successfully into SqliteDb_developers table")
        sqliteConnection.c..
        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to insert multiple records into sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("The SQLite connection is closed")

recordsToInsert _ [(4, 'Jos', 'jos@gmail.com', '2019-01-14', 9500),
                   (5, 'Chris', 'chris@gmail.com', '2019-05-15',7600),
                   (6, 'Jonny', 'jonny@gmail.com', '2019-03-27', 8400)]

insertMultipleRecords(recordsToInsert)


# Connected to SQLite
# Total 3 Records inserted successfully into SqliteDb_developers table
# The SQLite connection is closed