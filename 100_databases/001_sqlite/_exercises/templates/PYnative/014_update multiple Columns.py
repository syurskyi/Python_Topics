import sqlite3

def updateMultipleColumns(id, salary, email):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_update_query = """Update new_developers set salary = ?, email = ? where id = ?"""
        columnValues = (salary, email, id)
        cursor.execute(sqlite_update_query, columnValues)
        sqliteConnection.commit()
        print("Multiple columns updated successfully")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update multiple columns of sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

updateMultipleColumns(3, 6500, 'ben_stokes@gmail.com')


# Connected to SQLite
# Multiple columns updated successfully
# sqlite connection is closed

