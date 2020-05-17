#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ sqlite
_____ ___


def writeImage(data):
    fout _ None

    ___
        fout _ open('Camera.png', 'wb')
        fout.write(data)

    ______ IOError __ e:

        print(e)
        ___.exit(1)

    f__

        __ fout:
            fout.c..


con _ None

___
    con _ sqlite.c..('ydb.db')

    cur _ con.c..
    cur.e..("S.. data F.. images LIMIT 1")
    data _ cur.f_o..[0]

    writeImage(data)


______ sqlite.Error __ e:

    print(e)
    ___.exit(1)

f__

    __ con:
        con.c..
