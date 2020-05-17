#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

with con:

    cur _ con.c..
    cur.e..("""S.. table_name F.. information_schema.tables
        WHERE table_schema = 'public'""")

    rows _ cur.f_a..

    ___ row __ rows:
        print(row[0])


# $ list_tables.py
# cars
# countries
# projects
# employees
# users
# tasks
# images