#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

con = psycopg2.connect(database='testdb', user='syurskyi',
                       password='1234')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Audi', 52642)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Mercedes', 57127)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Skoda', 9000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Volvo', 29000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Bentley', 350000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Citroen', 21000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Hummer', 41400)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Volkswagen', 21600)")



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