#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite
_____ ___


def writeImage(data):
    fout _ None

    try:
        fout _ open('Camera.png', 'wb')
        fout.write(data)

    except IOError as e:

        print(e)
        ___.exit(1)

    finally:

        __ fout:
            fout.c..


con _ None

try:
    con _ sqlite.c..('ydb.db')

    cur _ con.c..
    cur.e..("S.. data F.. images LIMIT 1")
    data _ cur.f_o..[0]

    writeImage(data)


except sqlite.Error as e:

    print(e)
    ___.exit(1)

finally:

    __ con:
        con.c..
