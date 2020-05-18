_____ ?
_____ traceback
_____ sys

___
    sqliteConnection _ ?.c..('SQLite_Python.db')
    cursor _ ?.c..
    print("Successfully Connected to SQLite")

    sqlite_insert_query _ """I.. I.. unknown_table_1
                          (id, text)  V..  (1, 'Demo Text')"""

    count _ ?.e..(sqlite_insert_query)
    ?.c..
    print("Record inserted successfully into SqliteDb_developers table ", ?.r..
    ?.c..

_____ ?.E.. __ error:
    print("Failed to insert data into sqlite table")
    print("Exception class is: ", error.__class__)
    print("Exception is", error.args)
    print('Printing detailed SQLite exception traceback: ')
    exc_type, exc_value, exc_tb _ sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
f..
    __ (?
        ?.c..
        print("The SQLite connection is closed")


# Output:
#
# Successfully Connected to SQLite
# Failed to insert data into sqlite table
# Exception class is:  <class '?.OperationalError'>
# Exception is ('no such table: unknown_table_1',)
# Printing detailed SQLite exception traceback:
# ['Traceback (most recent call last\n', '  File "E:/demos/sqlite_demos/sqlite_errors.py", line 13, in <module>\n    count = cursor.execute(sqlite_insert_query)\n', '?.OperationalError: no such table: unknown_table_1\n']
# The SQLite connection is closed