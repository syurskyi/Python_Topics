#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

con = sqlite.connect('ydb.db')

with con:   # With the with keyword, the Python interpreter automatically releases the resources.
            # It also provides error handling.

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()[0]

    print(f"SQLite version: {data}")

# The script returns the current version of the SQLite database. With the use of the with keyword.
# The code is more compact.