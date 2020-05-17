#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ sqlite # _____ the sqlite3 and give it an alias.
_____ ___

con _ None  # We initialise the con variable to None.
            # In case we could not create a connection to the database
            # (for example the disk is full), we would not have a connection variable defined.
            # This would lead to an error in the finally clause.

___
    con _ sqlite.c..('ydb.db')  #  We connect to the ydb.db database. The connect() method returns a connection object.

    cur _ con.c..  # From the connection, we get the cursor object. The cursor is used to traverse the records from the result set.
    cur.e..('S.. SQLITE_VERSION()') # We call the execute() method of the cursor and execute the SQL statement.

    data _ cur.f_o..[0]  # We fetch the data. Since we retrieve only one record, we call the f_o.. method.

    print(f"SQLite version: {data}")  # We print the data that we have retrieved to the console.

______ sqlite.Error __ e:  # In case of an exception, we print an error message and exit the script with an error code 1.

    print(f"Error {e.args[0]}")
    ___.exit(1)

f__

    __ con:
        con.c..
