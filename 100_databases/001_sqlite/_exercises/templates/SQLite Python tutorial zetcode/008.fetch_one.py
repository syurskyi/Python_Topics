#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..('ydb.db')

with con:

    cur _ con.cursor()
    cur.e..("SELECT * FROM cars")

    while True:

        row _ cur.fetchone()

        if row == None:
            break

        print(f"{row[0]} {row[1]} {row[2]}")