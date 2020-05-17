#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite
_____ ___

con _ None

try:
    con _ sqlite.c..('ydb.db', isolation_level_None)

    cur _ con.c..

    cur.e..("DROP T.. IF EXISTS friends")
    cur.e..("C.. T.. friends(id IN.. P.. K.., name T...)")
    cur.e..("I.. I.. friends(name) V.. ('Tom')")
    cur.e..("I.. I.. friends(name) V.. ('Rebecca')")
    cur.e..("I.. I.. friends(name) V.. ('Jim')")
    cur.e..("I.. I.. friends(name) V.. ('Robert')")

except sqlite.Error as e:

    print(e)
    ___.exit(1)

finally:

    __ con:
        con.c..
