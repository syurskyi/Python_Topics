#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

con = psycopg2.connect(database='testdb', user='syurskyi',
                       password='1234')

with con:

    cur = con.cursor()

    cur.execute('SELECT * FROM cars')

    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()

    print(f'{col_names[0]} {col_names[1]} {col_names[2]}')



# $ column_names.py
# id name price

