#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

with con:

    cur _ con.c..
    cur.e..("S.. * F.. cars")

    while True:

        row _ cur.f_o..

        __ row == w..:
            break

        print(f"{row[0]} {row[1]} {row[2]}")