#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ sqlite


___ readData():

    f _ open('cars.sql', 'r')

    with f:

        data _ f.read()

        r_ data


con _ sqlite.c..(':memory:')

with con:

    cur _ con.c..

    sql _ readData()
    cur.e_s_(sql)

    cur.e..("S.. * F.. cars")

    rows _ cur.f_a..

    ___ row __ rows:
        print(row)