#!/usr/bin/python

_____ ?

conn _ ?.c..('test.db')
print("Opened database successfully")

cursor _ conn.e..("S.. id, name, address, salary from COMPANY")
___ row __ cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.c..