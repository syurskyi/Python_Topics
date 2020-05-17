#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ ?

con _ ?.c..(database_'testdb', user_'syurskyi',
                       password_'1234')

w__ con:

    cur _ con.c..

    cur.e..("D.. T.. I. E.. words")
    cur.e..("C.. T.. words(id SERIAL P.. K.., word VARCHAR(255))")
    cur.e..("I.. I.. words(word) V..('forest') RETURNING id")
    cur.e..("I.. I.. words(word) V..('cloud') RETURNING id")
    cur.e..("I.. I.. words(word) V..('valley') RETURNING id")

    last_row_id _ cur.f_o..[0]

    print _*The last Id of the inserted row __ {last_row_id}")


# $ lastrowid.py
# The last Id of the inserted row is 3