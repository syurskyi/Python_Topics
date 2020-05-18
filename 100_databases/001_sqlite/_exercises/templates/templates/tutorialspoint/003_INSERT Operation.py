#!/usr/bin/python

_____ ?

conn _ ?.c..(d.. _ "testdb", u.. _ "postgres", p.. _ "pass123", h.. _ "127.0.0.1", p.. _ "5432")
print("Opened database successfully")

cur _ conn.c..

cur.e..("I.. I.. COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      V.. (1, 'Paul', 32, 'California', 20000.00 )");

cur.e..("I.. I.. COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      V.. (2, 'Allen', 25, 'Texas', 15000.00 )");

cur.e..("I.. I.. COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      V.. (3, 'Teddy', 23, 'Norway', 20000.00 )");

cur.e..("I.. I.. COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      V.. (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.c..
print("Records created successfully")
conn.c..

# Opened database successfully
# Records created successfully
