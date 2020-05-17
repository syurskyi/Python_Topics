#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ sqlite

con _ sqlite.c..('ydb.db')

with con:

    cur _ con.c..
    cur.e..("S.. * F.. cars")

    while True:

        row _ cur.f_o..

        __ row == None:
            break

        print(f"{row[0]} {row[1]} {row[2]}")