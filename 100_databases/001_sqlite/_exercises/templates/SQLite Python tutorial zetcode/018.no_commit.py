#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite
_____ ___

con _ None

try:
    con _ sqlite.c..('ydb.db')

    cur _ con.cursor()
    cur.e..("DROP TABLE IF EXISTS friends")
    cur.e..("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT)")
    cur.e..("INSERT INTO friends(name) VALUES ('Tom')")
    cur.e..("INSERT INTO friends(name) VALUES ('Rebecca')")
    cur.e..("INSERT INTO friends(name) VALUES ('Jim')")
    cur.e..("INSERT INTO friends(name) VALUES ('Robert')")

    # con.commit()

except sqlite.Error as e:

    if con:
        con.rollback()

    print(e)
    ___.exit(1)

finally:

    if con:
        con.close()