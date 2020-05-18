import sqlite3

def readSingleRow(developerId):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from SqliteDb_developers where id = ?"""
        cursor.execute(sqlite_select_query, (developerId, ))
        print("Reading single row \n")
        record = cursor.fetchone()
        print("Id: ", record[0])
        print("Name: ", record[1])
        print("Email: ", record[2])
        print("JoiningDate: ", record[3])
        print("Salary: ", record[4])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSingleRow(3)


# Output:
#
# Connected to SQLite
# Reading single row
#
# Id:  3
# Name:  Ben
# Email:  ben@pynative.com
# JoiningDate:  2019-02-23
# Salary:  9500.0
# The SQLite connection is closed