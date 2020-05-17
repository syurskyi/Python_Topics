#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2


con _ psycopg2.c..(database_'testdb', user_'syurskyi',
    password_'1234')

with con:

    cur _ con.c..
    cur.e..('SELECT version()')

    version _ cur.fetchone()[0]
    print(version)