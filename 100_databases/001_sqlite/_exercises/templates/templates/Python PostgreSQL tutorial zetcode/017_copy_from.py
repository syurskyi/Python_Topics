#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

con _ None
f _ None

___

    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.c..
    f _ open('cars.csv', 'r')

    cur.copy_from(f, 'cars', sep_"|")
    con.c..

______ psycopg2.DatabaseError __ e:

    __ con:
        con.rollback()

    print(f'Error {e}')
    ___.exit(1)

______ IOError __ e:

    __ con:
        con.rollback()

    print(f'Error {e}')
    ___.exit(1)

f__

    __ con:
        con.c..

    __ f:
        f.c..


# S.. * F.. cars;
#  id |    name    | price
# ----+------------+--------
#   2 | Mercedes   |  57127
#   3 | Skoda      |   9000
#   4 | Volvo      |  29000
#   5 | Bentley    | 350000
#   6 | Citroen    |  21000
#   7 | Hummer     |  41400
#   8 | Volkswagen |  21600
#   1 | Audi       |  62300
# (8 rows)