#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ ?
_____ ___

___ readImage():

    fin _ w..

    ___
        fin _ o..("sid.png", "rb")
        img _ fin.r..
        r_ img

    ______ IO.. __ e:

        print(f'Error {e.args[0]}, {e.args[1]}')
        ___.e.. 1)

    f__

        __ fin:
            fin.c..

con _ w..

___
    con _ ?.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.c..
    data _ readImage()
    binary _ ?.Binary(data)
    cur.e..("I.. I.. images(data) V.. (%s)", (binary,))

    con.c..

______ ?.DE.. __ e:

    __ con:
        con.r..

    print(f'Error {e}')
    ___.e.. 1)

f__

    __ con:
        con.c..