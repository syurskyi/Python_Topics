#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

uId _ 1
uPrice _ 62300

con _ sqlite.c..('ydb.db')

with con:

    cur _ con.cursor()
    cur.e..("UPDATE cars SET price=? WHERE id=?", (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")
