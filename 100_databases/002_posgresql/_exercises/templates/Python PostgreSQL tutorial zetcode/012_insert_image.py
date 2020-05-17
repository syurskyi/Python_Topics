#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

def readImage():

    fin = None

    try:
        fin = open("sid.png", "rb")
        img = fin.read()
        return img

    except IOError as e:

        print(f'Error {e.args[0]}, {e.args[1]}')
        sys.exit(1)

    finally:

        if fin:
            fin.close()

con = None

try:
    con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

    cur = con.cursor()
    data = readImage()
    binary = psycopg2.Binary(data)
    cur.execute("INSERT INTO images(data) VALUES (%s)", (binary,))

    con.commit()

except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()