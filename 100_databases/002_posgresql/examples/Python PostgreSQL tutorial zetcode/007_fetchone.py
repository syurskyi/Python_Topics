#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        print(f"{row[0]} {row[1]} {row[2]}")