#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                       password_'1234')

with con:

    cur _ con.c..

    cur.e..("DROP T.. IF EXISTS words")
    cur.e..("C.. T.. words(id SERIAL P.. K.., word VARCHAR(255))")
    cur.e..("I.. I.. words(word) V..('forest') RETURNING id")
    cur.e..("I.. I.. words(word) V..('cloud') RETURNING id")
    cur.e..("I.. I.. words(word) V..('valley') RETURNING id")

    last_row_id _ cur.fetchone()[0]

    print(f"The last Id of the inserted row is {last_row_id}")


# $ lastrowid.py
# The last Id of the inserted row is 3