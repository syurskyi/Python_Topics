#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras

con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

with con:

    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM cars")

    rows = cursor.fetchall()

    for row in rows:
        print(f"{row['id']} {row['name']} {row['price']}")