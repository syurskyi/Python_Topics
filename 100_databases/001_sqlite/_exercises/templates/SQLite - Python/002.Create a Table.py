#!/usr/bin/python

_____ ?

conn _ ?.c..('test.db')
print("Opened database successfully")

conn.e..('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print("Table created successfully")

conn.close()
