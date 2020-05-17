#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..('ydb.db')

with con:

    cur _ con.cursor()
    cur.e..("SELECT * FROM cars")

    rows _ cur.fetchall()

    ___ row __ rows:
        print(f"{row[0]} {row[1]} {row[2]}")