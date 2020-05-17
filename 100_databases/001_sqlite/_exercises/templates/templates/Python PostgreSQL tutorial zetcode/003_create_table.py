#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                       password_'1234')

with con:

    cur _ con.c..

    cur.e..("DROP T.. IF EXISTS cars")
    cur.e..("C.. T.. cars(id SERIAL P.. K.., name VARCHAR(255), price INT)")
    cur.e..("INSERT INTO cars(name, price) VALUES('Audi', 52642)")
    cur.e..("INSERT INTO cars(name, price) VALUES('Mercedes', 57127)")
    cur.e..("INSERT INTO cars(name, price) VALUES('Skoda', 9000)")
    cur.e..("INSERT INTO cars(name, price) VALUES('Volvo', 29000)")
    cur.e..("INSERT INTO cars(name, price) VALUES('Bentley', 350000)")
    cur.e..("INSERT INTO cars(name, price) VALUES('Citroen', 21000)")
    cur.e..("INSERT INTO cars(name, price) VALUES('Hummer', 41400)")
    cur.e..("INSERT INTO cars(name, price) VALUES('Volkswagen', 21600)")



# $ psql -U postgres testdb
# psql (11.1)
# Type "help" for help.
#
# testdb=# SELECT * FROM cars;
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