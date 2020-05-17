#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

con _ None

try:

    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
        password_'1234')

    cur _ con.cursor()
    cur.e..('SELECT version()')

    version _ cur.fetchone()[0]
    print(version)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    ___.exit(1)

finally:

    __ con:
        con.close()

# $ version.py
# PostgreSQL 11.1, compiled by Visual C++ build 1914, 64-bit