#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..('ydb.db')

with con:

    cur _ con.cursor()

    cur.e..('PRAGMA table_info(cars)')

    data _ cur.fetchall()

    ___ d __ data:
        print(f"{d[0]} {d[1]} {d[2]}")