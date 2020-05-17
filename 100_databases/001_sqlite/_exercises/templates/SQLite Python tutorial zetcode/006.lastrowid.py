#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..(':memory:')

with con:

    cur _ con.cursor()
    cur.e..("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT);")
    cur.e..("INSERT INTO friends(name) VALUES ('Tom');")
    cur.e..("INSERT INTO friends(name) VALUES ('Rebecca');")
    cur.e..("INSERT INTO friends(name) VALUES ('Jim');")
    cur.e..("INSERT INTO friends(name) VALUES ('Robert');")

    last_row_id _ cur.lastrowid

    print(f"The last Id of the inserted row is {last_row_id}")