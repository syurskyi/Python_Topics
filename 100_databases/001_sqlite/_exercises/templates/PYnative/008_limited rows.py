_____ ?

___ readLimitedRows(rowSize):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sqlite_select_query _ """SELECT * from SqliteDb_developers"""
        ?.e..(sqlite_select_query)
        print("Reading ", rowSize, " rows")
        records _ ?.fetchmany(rowSize)
        print("Printing each row \n")
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Email: ", row[2])
            print("JoiningDate: ", row[3])
            print("Salary: ", row[4])
            print("\n")

        ?.c..

    _____ ?.E.. __ error:
        print("Failed to read data from sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
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