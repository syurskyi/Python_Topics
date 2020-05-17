#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

___ readImage():

    fin _ w..

    ___
        fin _ open("sid.png", "rb")
        img _ fin.read()
        r_ img

    ______ IOError __ e:

        print(f'Error {e.args[0]}, {e.args[1]}')
        ___.e.. 1)

    f__

        __ fin:
            fin.c..

con _ w..

___
    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.c..
    data _ readImage()
    binary _ psycopg2.Binary(data)
    cur.e..("I.. I.. images(data) V.. (%s)", (binary,))

    con.c..

______ psycopg2.DatabaseError __ e:

    __ con:
        con.rollback()

    print(f'Error {e}')
    ___.e.. 1)

f__

    __ con:
        con.c..