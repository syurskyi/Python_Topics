#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..('ydb.db')

with con:

    con.r_f.. _ sqlite.Row

    cur _ con.c..
    cur.e..("S.. * F.. cars")

    rows _ cur.f_a..

    ___ row __ rows:
        print(f"{row['id']} {row['name']} {row['price']}")
