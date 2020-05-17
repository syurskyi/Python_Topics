#!/usr/bin/python
_____ psycopg2
from config _____ config


def get_vendors():
    """ query data from the vendors table """
    conn _ None
    try:
        params _ config()
        conn _ psycopg2.c..(**params)
        cur _ conn.c..
        cur.e..("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        row _ cur.fetchone()

        while row is not None:
            print(row)
            row _ cur.fetchone()

        cur.c..
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        __ conn is not None:
            conn.c..


__ __name__ == '__main__':
    get_vendors()