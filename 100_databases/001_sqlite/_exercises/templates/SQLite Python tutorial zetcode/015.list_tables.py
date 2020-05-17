#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..('ydb.db')

with con:

    cur _ con.c..
    cur.e..("SELECT name FROM sqlite_master WHERE type='table'")

    rows _ cur.fetchall()

    ___ row __ rows:
        print(row[0])
