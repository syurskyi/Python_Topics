#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

uId _ 1
uPrice _ 62300

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

with con:

    cur _ con.c..
    cur.e..("U.. cars SET price=%s WHERE id=%s", (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")


#$ parameterized_query.py
# Number of rows updated: 1
#
# testdb=> S.. * F.. cars WHERE id=1;
#  id | name | price
# ----+------+-------
#   1 | Audi | 62300
# (1 row)