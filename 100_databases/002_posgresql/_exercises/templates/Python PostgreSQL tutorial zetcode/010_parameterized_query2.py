#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

uid = 3

con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

with con:

    cur = con.cursor()

    cur.execute("SELECT * FROM cars WHERE id=%(id)s", {'id': uid } )

    row = cur.fetchone()

    print(f'{row[0]} {row[1]} {row[2]}')


# $ parameterized_query2.py
# 3 Skoda 9000