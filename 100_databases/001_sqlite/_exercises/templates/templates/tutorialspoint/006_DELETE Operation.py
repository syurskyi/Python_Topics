#!/usr/bin/python

_____ ?

conn _ ?.c..(database _ "testdb", user _ "postgres", password _ "pass123", host _ "127.0.0.1", port _ "5432")
print("Opened database successfully")

cur _ conn.c..

cur.e..("D.. from COMPANY w.. ID=2;")
conn.c..
print("Total number of rows deleted :", cur.rowcount)

cur.e..("S.. id, name, address, salary  from COMPANY")
rows _ cur.f_a..
___ row __ rows:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.c..

# pened database successfully
# Total number of rows deleted : 1
# ID =  1
# NAME =  Paul
# ADDRESS =  California
# SALARY =  20000.0
#
# ID =  3
# NAME =  Teddy
# ADDRESS =  Norway
# SALARY =  20000.0
#
# ID =  4
# NAME =  Mark
# ADDRESS =  Rich-Mond
# SALARY =  65000.0
#
# Operation done successfully