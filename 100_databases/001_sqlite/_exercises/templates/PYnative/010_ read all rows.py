_____ ?

___ readSqliteTable
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")

        sqlite_select_query _ """S.. _ from SqliteDb_developers"""
        ?.e..(sqlite_select_query)
        records _ ?.f_a..
        print("Total rows are:  ", le.(records))
        print("Printing each row")
        ___ row __ records:
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
        __ (?):
            ?.c..
            print("The SQLite connection is closed")

readSqliteTable()


# Output:
#
# C:\Anaconda3\envs\demos\python.exe E:/demos/sqlite_demos/sqlite_select.py
# Connected to SQLite
# Total rows are:   6
#
# Printing each row
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
# Id:  3
# Name:  Ben
# Email:  ben@pynative.com
# JoiningDate:  2019-02-23
# Salary:  9500.0
#
# Id:  4
# Name:  Jos
# Email:  jos@gmail.com
# JoiningDate:  2019-01-14
# Salary:  9500.0
#
# Id:  5
# Name:  Chris
# Email:  chris@gmail.com
# JoiningDate:  2019-05-15
# Salary:  7600.0
#
# Id:  6
# Name:  Jonny
# Email:  jonny@gmail.com
# JoiningDate:  2019-03-27
# Salary:  8400.0
#
# The SQLite connection is closed