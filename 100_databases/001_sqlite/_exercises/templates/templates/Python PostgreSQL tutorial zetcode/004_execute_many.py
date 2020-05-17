#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

cars _ (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Citroen', 21000),
    (7, 'Hummer', 41400),
    (8, 'Volkswagen', 21600)
)

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

with con:

    cur _ con.c..

    cur.e..("DROP T.. IF EXISTS cars")
    cur.e..("C.. T.. cars(id SERIAL P.. K.., name VARCHAR(255), price INT)")

    query _ "I.. I.. cars (id, name, price) V.. (%s, %s, %s)"
    cur.e_m_(query, cars)

    con.c..
