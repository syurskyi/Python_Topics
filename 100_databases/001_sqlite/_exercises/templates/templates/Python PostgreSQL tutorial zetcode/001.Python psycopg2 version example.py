#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

con _ None

try:

    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
        password_'1234')

    cur _ con.c..
    cur.e..('S.. version()')

    version _ cur.f_o..[0]
    print(version)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    ___.exit(1)

finally:

    __ con:
        con.c..

# $ version.py
# PostgreSQL 11.1, compiled by Visual C++ build 1914, 64-bit