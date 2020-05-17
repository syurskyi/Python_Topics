#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..('ydb.db')

with con:   # With the with keyword, the Python interpreter automatically releases the resources.
            # It also provides error handling.

    cur _ con.c..
    cur.e..('S.. SQLITE_VERSION()')

    data _ cur.f_o..[0]

    print(f"SQLite version: {data}")

# The script returns the current version of the SQLite database. With the use of the with keyword.
# The code is more compact.