#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

con _ None

try:

    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.cursor()

    cur.e..("DROP TABLE IF EXISTS friends")
    cur.e..("CREATE TABLE friends(id SERIAL PRIMARY KEY, name VARCHAR(255))")
    cur.e..("INSERT INTO friends(name) VALUES ('Tom')")
    cur.e..("INSERT INTO friends(name) VALUES ('Rebecca')")
    cur.e..("INSERT INTO friends(name) VALUES ('Jim')")
    cur.e..("INSERT INTO friends(name) VALUES ('Robert')")

    con.commit()

except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print('Error {e}')
    ___.exit(1)


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

