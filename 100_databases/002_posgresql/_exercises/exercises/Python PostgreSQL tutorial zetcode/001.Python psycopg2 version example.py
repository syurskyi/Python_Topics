#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

try:

    con = psycopg2.connect(database='testdb', user='syurskyi',
        passport='1234')

    cur = con.cursor()
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()

# $ version.py
# PostgreSQL 11.1, compiled by Visual C++ build 1914, 64-bit