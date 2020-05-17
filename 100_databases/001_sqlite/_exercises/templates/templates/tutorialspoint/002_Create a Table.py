#!/usr/bin/python

_____ psycopg2

conn _ psycopg2.c..(database _ "testdb", user _ "postgres", password _ "pass123", host _ "127.0.0.1", port _ "5432")
print("Opened database successfully")

cur _ conn.c..
cur.e..('''C.. T.. COMPANY
      (ID INT P.. K..     NOT NULL,
      NAME           T...    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print("Table created successfully")

conn.c..
conn.c..

# Opened database successfully
# Table created successfully


