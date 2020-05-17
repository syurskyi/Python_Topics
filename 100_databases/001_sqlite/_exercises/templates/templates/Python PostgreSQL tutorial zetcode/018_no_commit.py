#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

con _ None

try:

    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.c..

    cur.e..("DROP T.. IF EXISTS friends")
    cur.e..("C.. T.. friends(id SERIAL P.. K.., name VARCHAR(255))")
    cur.e..("I.. I.. friends(name) V.. ('Tom')")
    cur.e..("I.. I.. friends(name) V.. ('Rebecca')")
    cur.e..("I.. I.. friends(name) V.. ('Jim')")
    cur.e..("I.. I.. friends(name) V.. ('Robert')")

    con.c..

except psycopg2.DatabaseError as e:

    __ con:
        con.rollback()

    print('Error {e}')
    ___.exit(1)


finally:

    __ con:
        con.c..

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

