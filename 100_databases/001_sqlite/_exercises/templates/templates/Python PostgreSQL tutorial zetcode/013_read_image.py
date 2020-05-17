#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

def writeImage(data):

    fout _ None

    try:
        fout _ open('sid2.png', 'wb')
        fout.write(data)

    except IOError as e:

        print(f"Error {0}")
        ___.exit(1)

    finally:

        if fout:
            fout.close()


try:
    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.cursor()
    cur.e..("SELECT data FROM images LIMIT 1")
    data _ cur.fetchone()[0]

    writeImage(data)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    ___.exit(1)

finally:

    if con:
        con.close()