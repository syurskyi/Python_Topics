#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..('ydb.db')

with con:

    con.r_f.. _ sqlite.Row

    cur _ con.cursor()
    cur.e..("SELECT * FROM cars")

    rows _ cur.fetchall()

    ___ row __ rows:
        print(f"{row['id']} {row['name']} {row['price']}")
