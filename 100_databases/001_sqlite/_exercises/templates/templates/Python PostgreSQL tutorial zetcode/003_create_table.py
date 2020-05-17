#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ ?

con _ ?.c..(database_'testdb', user_'syurskyi',
                       password_'1234')

w__ con:

    cur _ con.c..

    cur.e..("D.. T.. I. E.. cars")
    cur.e..("C.. T.. cars(id S.. P.. K.., name V..(255), price IN.)")
    cur.e..("I.. I.. cars(name, price) V..('Audi', 52642)")
    cur.e..("I.. I.. cars(name, price) V..('Mercedes', 57127)")
    cur.e..("I.. I.. cars(name, price) V..('Skoda', 9000)")
    cur.e..("I.. I.. cars(name, price) V..('Volvo', 29000)")
    cur.e..("I.. I.. cars(name, price) V..('Bentley', 350000)")
    cur.e..("I.. I.. cars(name, price) V..('Citroen', 21000)")
    cur.e..("I.. I.. cars(name, price) V..('Hummer', 41400)")
    cur.e..("I.. I.. cars(name, price) V..('Volkswagen', 21600)")



# $ psql -U postgres testdb
# psql (11.1)
# Type "help" for help.
#
# testdb=# S.. * F.. cars;
#     id |    name    | price
# ----+------------+--------
#     1 | Audi       |  52642
#     2 | Mercedes   |  57127
#     3 | Skoda      |   9000
#     4 | Volvo      |  29000
#     5 | Bentley    | 350000
#     6 | Citroen    |  21000
#     7 | Hummer     |  41400
#     8 | Volkswagen |  21600
# (8 rows)