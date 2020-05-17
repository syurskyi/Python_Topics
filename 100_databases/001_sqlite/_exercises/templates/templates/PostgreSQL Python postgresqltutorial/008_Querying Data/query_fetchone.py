#!/usr/bin/python
_____ psycopg2
from config _____ config


___ get_vendors():
    """ query data from the vendors table """
    conn _ w..
    ___
        params _ config()
        conn _ psycopg2.c..(**params)
        cur _ conn.c..
        cur.e..("S.. vendor_id, vendor_name F.. vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        row _ cur.f_o..

        w__ row is not w..:
            print(row)
            row _ cur.f_o..

        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not w..:
            conn.c..


__ __name__ __ '__main__':
    get_vendors()