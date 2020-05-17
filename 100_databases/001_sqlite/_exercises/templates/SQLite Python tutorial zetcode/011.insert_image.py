#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ ?
_____ ___

___ readImage():

    fin _ w..

    ___
        fin _ open("Camera.png", "rb")
        img _ fin.read()
        r_ img

    ______ IOError __ e:

        print(e)
        ___.e.. 1)

    f__

        __ fin:
            fin.c..

con _ w..

___
    con _ ?.c..('ydb.db')

    cur _ con.c..

    data _ readImage()
    binary _ ?.Binary(data)
    cur.e..("I.. I.. images(data) V.. (?)", (binary,) )

    con.c..

______ ?.Er.. __ e:

    __ con:
        con.rollback()

    print(e)
    ___.e.. 1)

f__

    __ con:
        con.c..