#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

uid _ 3

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

w__ con:

    cur _ con.c..

    cur.e..("S.. * F.. cars WHERE id=%(id)s", {'id': uid } )

    row _ cur.f_o..

    print(f'{row[0]} {row[1]} {row[2]}')


# $ parameterized_query2.py
# 3 Skoda 9000