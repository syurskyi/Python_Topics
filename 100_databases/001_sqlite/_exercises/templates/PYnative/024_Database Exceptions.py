import sqlite3
import traceback
import sys

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO unknown_table_1
                          (id, text)  VALUES  (1, 'Demo Text')"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table")
    print("Exception class is: ", error.__class__)
    print("Exception is", error.args)
    print('Printing detailed SQLite exception traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")


# Output:
#
# Successfully Connected to SQLite
# Failed to insert data into sqlite table
# Exception class is:  <class 'sqlite3.OperationalError'>
# Exception is ('no such table: unknown_table_1',)
# Printing detailed SQLite exception traceback:
# ['Traceback (most recent call last):\n', '  File "E:/demos/sqlite_demos/sqlite_errors.py", line 13, in <module>\n    count = cursor.execute(sqlite_insert_query)\n', 'sqlite3.OperationalError: no such table: unknown_table_1\n']
# The SQLite connection is closed