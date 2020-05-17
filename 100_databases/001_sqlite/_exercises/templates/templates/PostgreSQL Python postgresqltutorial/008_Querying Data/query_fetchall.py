#!/usr/bin/python
_____ psycopg2
from config _____ config

___ get_parts():
    """ query parts from the parts table """
    conn _ None
    ___
        params _ config()
        conn _ psycopg2.c..(**params)
        cur _ conn.c..
        cur.e..("S.. part_id, part_name F.. parts ORDER BY part_name")
        rows _ cur.f_a..
        print("The number of parts: ", cur.rowcount)
        ___ row __ rows:
            print(row)
        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not None:
            conn.c..

__ __name__ == '__main__':
    get_parts()