#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                       password_'1234')
cur _ None

with con:
    cur _ con.c..

    print(cur.mogrify("SELECT name, price FROM cars WHERE id=%s", (2,)))

    # cur.execute("SELECT name, price FROM cars WHERE id=%s", (2,) )
    # row = cur.fetchone()
    # print(f"{row[0]} {row[1]}")



# $ mogrify.py
# b'SELECT name, price FROM cars WHERE id=2'
#
# This is the output.