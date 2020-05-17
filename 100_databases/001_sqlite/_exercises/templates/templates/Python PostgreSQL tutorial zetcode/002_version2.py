#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2


con _ psycopg2.c..(database_'testdb', user_'syurskyi',
    password_'1234')

w__ con:

    cur _ con.c..
    cur.e..('S.. version()')

    version _ cur.f_o..[0]
    print(version)