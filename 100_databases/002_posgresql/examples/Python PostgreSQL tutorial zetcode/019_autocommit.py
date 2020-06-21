#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

try:

    con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

    con.autocommit = True

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS friends")
    cur.execute("CREATE TABLE friends(id serial PRIMARY KEY, name VARCHAR(10))")
    cur.execute("INSERT INTO friends(name) VALUES ('Jane')")
    cur.execute("INSERT INTO friends(name) VALUES ('Tom')")
    cur.execute("INSERT INTO friends(name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO friends(name) VALUES ('Jim')")
    cur.execute("INSERT INTO friends(name) VALUES ('Robert')")
    cur.execute("INSERT INTO friends(name) VALUES ('Patrick')")


except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()


# $ autocommit.py
#
# testdb=# select * from friends;
#  id |  name
# ----+---------
#   1 | Jane
#   2 | Tom
#   3 | Rebecca
#   4 | Jim
#   5 | Robert
#   6 | Patrick
# (6 rows)