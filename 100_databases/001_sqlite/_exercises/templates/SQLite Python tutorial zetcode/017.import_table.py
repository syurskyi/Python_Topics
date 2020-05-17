#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ ?


___ readData():

    f _ o..('cars.sql', 'r')

    w__ f:

        data _ f.r..

        r_ data


con _ ?.c..(':memory:')

w__ con:

    cur _ con.c..

    sql _ readData()
    cur.e_s_(sql)

    cur.e..("S.. * F.. cars")

    rows _ cur.f_a..

    ___ row __ rows:
        print(row)