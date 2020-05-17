#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

def readImage():

    fin _ None

    try:
        fin _ open("sid.png", "rb")
        img _ fin.read()
        return img

    except IOError as e:

        print(f'Error {e.args[0]}, {e.args[1]}')
        ___.exit(1)

    finally:

        __ fin:
            fin.c..

con _ None

try:
    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.c..
    data _ readImage()
    binary _ psycopg2.Binary(data)
    cur.e..("INSERT INTO images(data) VALUES (%s)", (binary,))

    con.c..

except psycopg2.DatabaseError as e:

    __ con:
        con.rollback()

    print(f'Error {e}')
    ___.exit(1)

finally:

    __ con:
        con.c..