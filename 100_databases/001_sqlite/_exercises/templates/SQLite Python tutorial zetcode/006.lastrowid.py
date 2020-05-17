#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..(':memory:')

with con:

    cur _ con.c..
    cur.e..("C.. T.. friends(id IN.. P.. K.., name T...);")
    cur.e..("I.. I.. friends(name) V.. ('Tom');")
    cur.e..("I.. I.. friends(name) V.. ('Rebecca');")
    cur.e..("I.. I.. friends(name) V.. ('Jim');")
    cur.e..("I.. I.. friends(name) V.. ('Robert');")

    last_row_id _ cur.lastrowid

    print(f"The last Id of the inserted row is {last_row_id}")