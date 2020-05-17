#!/usr/bin/python

_____ ?

conn _ ?.c..('test.db')
print("Opened database successfully")

conn.e..("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.c..
print("Total number of rows updated :", conn.total_changes)

cursor _ conn.e..("SELECT id, name, address, salary from COMPANY")
___ row __ cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.c..
