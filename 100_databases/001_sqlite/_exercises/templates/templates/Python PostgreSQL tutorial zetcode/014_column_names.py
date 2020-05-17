#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                       password_'1234')

w__ con:

    cur _ con.c..

    cur.e..('S.. * F.. cars')

    col_names _ [cn[0] ___ cn __ cur.description]
    rows _ cur.f_a..

    print(f'{col_names[0]} {col_names[1]} {col_names[2]}')



# $ column_names.py
# id name price

