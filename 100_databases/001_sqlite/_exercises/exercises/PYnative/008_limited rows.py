import sqlite3

def readLimitedRows(rowSize):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * FROM SqliteDb_developers"""
        cursor.execute(sqlite_select_query)
        print("Reading ", rowSize, " rows")
        records = cursor.fetchmany(rowSize)
        print("Printing each row \n")
        for row in records:
            print("Id: ", row[0]),
            print("Name: ",  row[1]),
            print("Email: ", row[2]),
            print("JoiningDate: ", row[3]),
            print("Salary: ", row[4]),
            print("\n")

        cursor.close()

    except sqlite3.Erroe as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readLimitedRows(2)

# Output:
#
# Connected to SQLite
# Reading 2  rows
# Printing each row
#
# Id:  1
# Name:  James
# Email:  james@pynative.com
# JoiningDate:  2019-03-17
# Salary:  8000.0
#
# Id:  2
# Name:  Joe
# Email:  joe@pynative.com
# JoiningDate:  2019-05-19
# Salary:  9000.0
#
# The SQLite connection is closed