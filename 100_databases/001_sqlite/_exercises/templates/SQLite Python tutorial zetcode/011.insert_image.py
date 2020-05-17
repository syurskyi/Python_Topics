#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ sqlite
_____ ___

def readImage():

    fin _ None

    ___
        fin _ open("Camera.png", "rb")
        img _ fin.read()
        return img

    ______ IOError __ e:

        print(e)
        ___.exit(1)

    f__

        __ fin:
            fin.c..

con _ None

___
    con _ sqlite.c..('ydb.db')

    cur _ con.c..

    data _ readImage()
    binary _ sqlite.Binary(data)
    cur.e..("I.. I.. images(data) V.. (?)", (binary,) )

    con.c..

______ sqlite.Error __ e:

    __ con:
        con.rollback()

    print(e)
    ___.exit(1)

f__

    __ con:
        con.c..