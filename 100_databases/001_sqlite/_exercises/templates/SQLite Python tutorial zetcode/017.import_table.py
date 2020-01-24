#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite


def readData():

    f = open('cars.sql', 'r')

    with f:

        data = f.read()

        return data


con = sqlite.connect(':memory:')

with con:

    cur = con.cursor()

    sql = readData()
    cur.executescript(sql)

    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(row)