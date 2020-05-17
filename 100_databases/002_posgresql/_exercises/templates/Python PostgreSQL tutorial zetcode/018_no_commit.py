#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

try:

    con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS friends")
    cur.execute("CREATE TABLE friends(id SERIAL PRIMARY KEY, name VARCHAR(255))")
    cur.execute("INSERT INTO friends(name) VALUES ('Tom')")
    cur.execute("INSERT INTO friends(name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO friends(name) VALUES ('Jim')")
    cur.execute("INSERT INTO friends(name) VALUES ('Robert')")

    con.commit()

except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print('Error {e}')
    sys.exit(1)


finally:

    if con:
        con.close()

# testdb=# \dt
#         List of relations
# Schema |   Name    | Type  |  Owner
# --------+-----------+-------+----------
# public | cars      | table | postgres
# public | countries | table | postgres
# public | employees | table | postgres
# public | images    | table | postgres
# public | projects  | table | postgres
# public | tasks     | table | postgres
# public | users     | table | postgres
# (7 rows)'

