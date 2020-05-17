#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite
_____ ___

con _ None

try:
    con _ sqlite.c..('ydb.db')

    cur _ con.c..
    cur.e..("DROP T.. IF EXISTS friends")
    cur.e..("C.. T.. friends(id IN.. P.. K.., name T...)")
    cur.e..("I.. I.. friends(name) V.. ('Tom')")
    cur.e..("I.. I.. friends(name) V.. ('Rebecca')")
    cur.e..("I.. I.. friends(name) V.. ('Jim')")
    cur.e..("I.. I.. friends(name) V.. ('Robert')")

    # con.c..

except sqlite.Error as e:

    __ con:
        con.rollback()

    print(e)
    ___.exit(1)

finally:

    __ con:
        con.c..