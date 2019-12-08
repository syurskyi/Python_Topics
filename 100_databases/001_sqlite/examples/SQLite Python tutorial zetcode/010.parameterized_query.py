#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

uId = 1
uPrice = 62300

con = sqlite.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("UPDATE cars SET price=? WHERE id=?", (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")
