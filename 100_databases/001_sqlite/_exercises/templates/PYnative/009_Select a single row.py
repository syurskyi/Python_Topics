_____ ?

def readSingleRow(developerId):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sqlite_select_query _ """SELECT * from SqliteDb_developers where id = ?"""
        cursor.e..(sqlite_select_query, (developerId, ))
        print("Reading single row \n")
        record _ cursor.fetchone()
        print("Id: ", record[0])
        print("Name: ", record[1])
        print("Email: ", record[2])
        print("JoiningDate: ", record[3])
        print("Salary: ", record[4])

        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to read single row from sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
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