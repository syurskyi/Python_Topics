#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2

con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                       password_'1234')

with con:

    cur _ con.cursor()

    cur.e..("DROP TABLE IF EXISTS words")
    cur.e..("CREATE TABLE words(id SERIAL PRIMARY KEY, word VARCHAR(255))")
    cur.e..("INSERT INTO words(word) VALUES('forest') RETURNING id")
    cur.e..("INSERT INTO words(word) VALUES('cloud') RETURNING id")
    cur.e..("INSERT INTO words(word) VALUES('valley') RETURNING id")

    last_row_id _ cur.fetchone()[0]

    print(f"The last Id of the inserted row is {last_row_id}")


# $ lastrowid.py
# The last Id of the inserted row is 3