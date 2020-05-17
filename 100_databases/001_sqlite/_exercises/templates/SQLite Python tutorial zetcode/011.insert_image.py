#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite
_____ ___

def readImage():

    fin _ None

    try:
        fin _ open("Camera.png", "rb")
        img _ fin.read()
        return img

    except IOError as e:

        print(e)
        ___.exit(1)

    finally:

        __ fin:
            fin.c..

con _ None

try:
    con _ sqlite.c..('ydb.db')

    cur _ con.c..

    data _ readImage()
    binary _ sqlite.Binary(data)
    cur.e..("INSERT INTO images(data) VALUES (?)", (binary,) )

    con.c..

except sqlite.Error as e:

    __ con:
        con.rollback()

    print(e)
    ___.exit(1)

finally:

    __ con:
        con.c..