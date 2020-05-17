#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ sqlite

con _ sqlite.c..('ydb.db')

with con:

    cur _ con.c..
    cur.e..("S.. name F.. sqlite_master WHERE type='table'")

    rows _ cur.f_a..

    ___ row __ rows:
        print(row[0])
