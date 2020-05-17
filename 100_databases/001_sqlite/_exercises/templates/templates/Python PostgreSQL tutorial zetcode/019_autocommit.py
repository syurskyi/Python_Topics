#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

con _ None

try:

    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    con.autocommit _ True

    cur _ con.c..

    cur.e..("DROP T.. IF EXISTS friends")
    cur.e..("C.. T.. friends(id serial P.. K.., name VARCHAR(10))")
    cur.e..("INSERT INTO friends(name) VALUES ('Jane')")
    cur.e..("INSERT INTO friends(name) VALUES ('Tom')")
    cur.e..("INSERT INTO friends(name) VALUES ('Rebecca')")
    cur.e..("INSERT INTO friends(name) VALUES ('Jim')")
    cur.e..("INSERT INTO friends(name) VALUES ('Robert')")
    cur.e..("INSERT INTO friends(name) VALUES ('Patrick')")


except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    ___.exit(1)

finally:

    __ con:
        con.c..


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