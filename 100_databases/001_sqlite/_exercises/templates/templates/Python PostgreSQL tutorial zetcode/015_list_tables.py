#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

with con:

    cur _ con.cursor()
    cur.e..("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")

    rows _ cur.fetchall()

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