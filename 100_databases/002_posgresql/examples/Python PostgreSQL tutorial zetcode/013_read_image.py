#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

def writeImage(data):

    fout = None

    try:
        fout = open('sid2.png', 'wb')
        fout.write(data)

    except IOError as e:

        print(f"Error {0}")
        sys.exit(1)

    finally:

        if fout:
            fout.close()


try:
    con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

    cur = con.cursor()
    cur.execute("SELECT data FROM images LIMIT 1")
    data = cur.fetchone()[0]

    writeImage(data)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()