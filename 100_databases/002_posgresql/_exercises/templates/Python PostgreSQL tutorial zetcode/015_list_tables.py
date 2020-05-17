#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

with con:

    cur = con.cursor()
    cur.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")

    rows = cur.fetchall()

    for row in rows:
        print(row[0])


# $ list_tables.py
# cars
# countries
# projects
# employees
# users
# tasks
# images