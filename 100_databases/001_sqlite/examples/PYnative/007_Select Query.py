import sqlite3

def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from SqliteDb_developers where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            print("Name = ", row[1])
            print("Email  = ", row[2])
            print("JoiningDate  = ", row[3])
            print("Salary  = ", row[4])
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(2)


# Connected to SQLite
# Printing ID  2
# Name =  Joe
# Email  =  joe@pynative.com
# JoiningDate  =  2019-05-19
# Salary  =  9000.0
# The SQLite connection is closed