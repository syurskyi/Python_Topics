_____ ?

def getDeveloperInfo(id):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sql_select_query _ """select * from SqliteDb_developers where id = ?"""
        ?.e..(sql_select_query, (id,))
        records _ ?.f_a..
        print("Printing ID ", id)
        for row in records:
            print("Name = ", row[1])
            print("Email  = ", row[2])
            print("JoiningDate  = ", row[3])
            print("Salary  = ", row[4])
        ?.c..

    _____ ?.E.. __ error:
        print("Failed to read data from sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("The SQLite connection is closed")

getDeveloperInfo(2)


# Connected to SQLite
# Printing ID  2
# Name =  Joe
# Email  =  joe@pynative.com
# JoiningDate  =  2019-05-19
# Salary  =  9000.0
# The SQLite connection is closed