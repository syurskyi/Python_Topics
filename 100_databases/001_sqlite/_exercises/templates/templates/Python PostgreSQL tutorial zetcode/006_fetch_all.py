#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syursky',
                    password_'1234')

with con:

    cur _ con.c..
    cur.e..("S.. * F.. cars")

    rows _ cur.f_a..

    ___ row __ rows:
        print(f"{row[0]} {row[1]} {row[2]}")



#  We print the data to the console, row by row.
#
# $ fetch_all.py
# 1 Audi 52642
# 2 Mercedes 57127
# 3 Skoda 9000
# 4 Volvo 29000
# 5 Bentley 350000
# 6 Citroen 21000
# 7 Hummer 41400
# 8 Volkswagen 21600