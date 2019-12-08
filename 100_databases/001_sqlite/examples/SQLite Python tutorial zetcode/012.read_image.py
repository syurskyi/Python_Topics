#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
import sys


def writeImage(data):
    fout = None

    try:
        fout = open('Camera.png', 'wb')
        fout.write(data)

    except IOError as e:

        print(e)
        sys.exit(1)

    finally:

        if fout:
            fout.close()


con = None

try:
    con = sqlite.connect('ydb.db')

    cur = con.cursor()
    cur.execute("SELECT data FROM images LIMIT 1")
    data = cur.fetchone()[0]

    writeImage(data)


except sqlite.Error as e:

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
