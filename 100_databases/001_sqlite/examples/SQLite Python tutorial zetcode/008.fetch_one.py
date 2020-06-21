#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

con = sqlite.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        print(f"{row[0]} {row[1]} {row[2]}")