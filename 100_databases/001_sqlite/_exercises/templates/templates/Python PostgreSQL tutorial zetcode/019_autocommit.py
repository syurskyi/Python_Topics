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
    cur.e..("I.. I.. friends(name) V.. ('Jane')")
    cur.e..("I.. I.. friends(name) V.. ('Tom')")
    cur.e..("I.. I.. friends(name) V.. ('Rebecca')")
    cur.e..("I.. I.. friends(name) V.. ('Jim')")
    cur.e..("I.. I.. friends(name) V.. ('Robert')")
    cur.e..("I.. I.. friends(name) V.. ('Patrick')")


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