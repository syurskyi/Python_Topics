#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

uid _ 3

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

with con:

    cur _ con.c..

    cur.e..("SELECT * FROM cars WHERE id=%(id)s", {'id': uid } )

    row _ cur.fetchone()

    print(f'{row[0]} {row[1]} {row[2]}')


# $ parameterized_query2.py
# 3 Skoda 9000