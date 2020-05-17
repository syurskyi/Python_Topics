#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                       password_'1234')
cur _ w..

w__ con:
    cur _ con.c..

    print(cur.mogrify("S.. name, price F.. cars WHERE id=%s", (2,)))

    # cur.execute("S.. name, price F.. cars WHERE id=%s", (2,) )
    # row = cur.f_o..
    # print(f"{row[0]} {row[1]}")



# $ mogrify.py
# b'S.. name, price F.. cars WHERE id=2'
#
# This is the output.