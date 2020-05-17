#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

___ writeImage(data):

    fout _ w..

    ___
        fout _ open('sid2.png', 'wb')
        fout.write(data)

    ______ IOError __ e:

        print(f"Error @")
        ___.e.. 1)

    f__

        __ fout:
            fout.c..


___
    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.c..
    cur.e..("S.. data F.. images LIMIT 1")
    data _ cur.f_o..[0]

    writeImage(data)

______ psycopg2.DatabaseError __ e:

    print(f'Error {e}')
    ___.e.. 1)

f__

    __ con:
        con.c..