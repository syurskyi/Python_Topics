#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

uId = 1
uPrice = 62300

con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

with con:

    cur = con.cursor()
    cur.execute("UPDATE cars SET price=%s WHERE id=%s", (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")


#$ parameterized_query.py
# Number of rows updated: 1
#
# testdb=> SELECT * FROM cars WHERE id=1;
#  id | name | price
# ----+------+-------
#   1 | Audi | 62300
# (1 row)