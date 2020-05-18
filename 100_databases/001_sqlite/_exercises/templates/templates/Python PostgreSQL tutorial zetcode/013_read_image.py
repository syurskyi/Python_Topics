#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ ?
_____ ___

___ writeImage(data):

    fout _ w..

    ___
        fout _ o..('sid2.png', 'wb')
        fout.write(data)

    ______ IO.. __ e:

        print _*Error @")
        ___.e.. 1)

    f__

        __ fout:
            fout.c..


___
    con _ ?.c..(d.._'testdb', u.._'syurskyi',
                    p.._'1234')

    cur _ con.c..
    cur.e..("S.. data F.. images LIMIT 1")
    data _ cur.f_o..[0]

    writeImage(data)

______ ?.DE.. __ e:

    print(f'Error {e}')
    ___.e.. 1)

f__

    __ con:
        con.c..