#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ ?

con _ ?.c..('ydb.db')

with con:

    cur _ con.c..
    cur.e..('S.. * F.. cars')

    col_names _ [cn[0] ___ cn __ cur.description]

    rows _ cur.f_a..

    print(f"{col_names[0]:3} {col_names[1]:10} {col_names[2]:7}")

    ___ row __ rows:
        print(f"{row[0]:<3} {row[1]:<10} {row[2]:7}")