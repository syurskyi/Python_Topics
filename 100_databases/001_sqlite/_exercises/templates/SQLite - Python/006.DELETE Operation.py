#!/usr/bin/python

_____ ?

conn _ ?.c..('test.db')
print("Opened database successfully")

conn.e..("DELETE from COMPANY where ID = 2;")
conn.c..
print("Total number of rows deleted :", conn.total_changes)

cursor _ conn.e..("SELECT id, name, address, salary from COMPANY")
___ row __ cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.c..