import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                           VALUES 
                          (1,'James','james@pynative.com','2019-03-17',8000)"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

# Successfully Connected to SQLite
# Record inserted successfully into SqliteDb_developers table
# The SQLite connection is closed