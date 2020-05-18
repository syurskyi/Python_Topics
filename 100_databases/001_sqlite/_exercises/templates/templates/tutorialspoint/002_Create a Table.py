#!/usr/bin/python

_____ ?

conn _ ?.c..(d.. _ "testdb", u.. _ "postgres", p.. _ "pass123", h.. _ "127.0.0.1", p.. _ "5432")
print("Opened database successfully")

cur _ conn.c..
cur.e..('''C.. T.. COMPANY
      (ID IN. P.. K..     N.. N..,
      NAME           T...    N.. N..,
      AGE            IN.     N.. N..,
      ADDRESS        CH..(50),
      SALARY         RE.);''')
print("Table created successfully")

conn.c..
conn.c..

# Opened database successfully
# Table created successfully


