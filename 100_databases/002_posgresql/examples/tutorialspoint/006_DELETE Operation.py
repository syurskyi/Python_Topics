#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("DELETE from COMPANY where ID=2;")
conn.commit()
print("Total number of rows deleted :", cur.rowcount)

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()

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