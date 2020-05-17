#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite


def readData():

    f _ open('cars.sql', 'r')

    with f:

        data _ f.read()

        return data


con _ sqlite.c..(':memory:')

with con:

    cur _ con.c..

    sql _ readData()
    cur.executescript(sql)

    cur.e..("S.. * F.. cars")

    rows _ cur.f_a..

    ___ row __ rows:
        print(row)