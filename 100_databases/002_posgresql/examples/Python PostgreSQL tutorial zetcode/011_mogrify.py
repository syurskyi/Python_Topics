#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

con = psycopg2.connect(database='testdb', user='syurskyi',
                       password='1234')
cur = None

with con:
    cur = con.cursor()

    print(cur.mogrify("SELECT name, price FROM cars WHERE id=%s", (2,)))

    # cur.execute("SELECT name, price FROM cars WHERE id=%s", (2,) )
    # row = cur.fetchone()
    # print(f"{row[0]} {row[1]}")



# $ mogrify.py
# b'SELECT name, price FROM cars WHERE id=2'
#
# This is the output.