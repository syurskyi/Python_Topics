import sqlite3

def updateSqliteTable(id, salary):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update SqliteDb_developers set salary = ? where id = ?"""
        data = (salary, id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The sqlite connection is closed")

updateSqliteTable(3, 7500)


# Connected to SQLite
# Record Updated successfully
# The sqlite connection is closed