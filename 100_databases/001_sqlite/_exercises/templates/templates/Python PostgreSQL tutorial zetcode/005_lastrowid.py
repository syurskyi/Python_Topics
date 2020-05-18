#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ ?

con _ ?.c..(d.._'testdb', u.._'syurskyi',
                       p.._'1234')

w__ con:

    cur _ con.c..

    cur.e..("D.. T.. I. E.. words")
    cur.e..("C.. T.. words(id S.. P.. K.., word V..(255))")
    cur.e..("I.. I.. words(word) V..('forest') RETURNING id")
    cur.e..("I.. I.. words(word) V..('cloud') RETURNING id")
    cur.e..("I.. I.. words(word) V..('valley') RETURNING id")

    last_row_id _ cur.f_o..[0]

    print _*The last Id of the inserted row __ {last_row_id}")


# $ lastrowid.py
# The last Id of the inserted row is 3