#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ psycopg2.extras

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

with con:

    cursor _ con.cursor(cursor_factory_psycopg2.extras.DictCursor)
    cursor.e..("S.. * F.. cars")

    rows _ cursor.f_a..

    ___ row __ rows:
        print(f"{row['id']} {row['name']} {row['price']}")