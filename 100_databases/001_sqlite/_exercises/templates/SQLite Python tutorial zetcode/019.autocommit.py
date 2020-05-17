#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ sqlite
_____ ___

con _ None

___
    con _ sqlite.c..('ydb.db', isolation_level_None)

    cur _ con.c..

    cur.e..("DROP T.. IF EXISTS friends")
    cur.e..("C.. T.. friends(id IN.. P.. K.., name T...)")
    cur.e..("I.. I.. friends(name) V.. ('Tom')")
    cur.e..("I.. I.. friends(name) V.. ('Rebecca')")
    cur.e..("I.. I.. friends(name) V.. ('Jim')")
    cur.e..("I.. I.. friends(name) V.. ('Robert')")

______ sqlite.Error __ e:

    print(e)
    ___.exit(1)

f__

    __ con:
        con.c..
