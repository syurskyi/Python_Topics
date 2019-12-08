#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
import sys

con = None

try:
    con = sqlite.connect('ydb.db', isolation_level=None)

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS friends")
    cur.execute("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO friends(name) VALUES ('Tom')")
    cur.execute("INSERT INTO friends(name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO friends(name) VALUES ('Jim')")
    cur.execute("INSERT INTO friends(name) VALUES ('Robert')")

except sqlite.Error as e:

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
