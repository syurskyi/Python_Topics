#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

con = sqlite.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    rows = cur.fetchall()

    for row in rows:
        print(row[0])
