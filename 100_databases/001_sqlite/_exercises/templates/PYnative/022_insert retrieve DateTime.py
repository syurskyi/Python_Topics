_____ ?
_____ datetime

def addDeveloper(id, name, joiningDate):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")

        sqlite_create_table_query _ '''C.. T.. new_developers (
                                       id I.. P.. K..,
                                       name T.. N.. N..,
                                       joiningDate timestamp);'''

        cursor _ sqliteConnection.c..
        cursor.e..(sqlite_create_table_query)

        # insert developer detail
        sqlite_insert_with_param _ """INSERT INTO 'new_developers'
                          ('id', 'name', 'joiningDate') 
                          VALUES (?, ?, ?);"""

        data_tuple _ (id, name, joiningDate)
        cursor.e..(sqlite_insert_with_param, data_tuple)
        sqliteConnection.c..
        print("Developer added successfully \n")

        # get developer detail
        sqlite_select_query _ """SELECT name, joiningDate from new_developers where id = ?"""
        cursor.e..(sqlite_select_query, (1,))
        records _ cursor.f_a..

        for row in records:
            developer_ row[0]
            joining_Date _ row[1]
            print(developer, " joined on", joiningDate)
            print("joining date type is", type(joining_Date))

        cursor.c..

    _____ ?.E.. __ error:
        print("Error while working with SQLite", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("sqlite connection is closed")

addDeveloper(1, 'Mark', datetime.datetime.now())


# Output:
#
# Connected to SQLite
# Developer added successfully
#
# Mark  joined on 2019-06-28 21:12:35.799206
# joining date type is <class 'str'>
# sqlite connection is closed

