#!/usr/bin/python
_____ psycopg2
from config _____ config


def iter_row(cursor, size_10):
    while True:
        rows _ cursor.fetchmany(size)
        __ not rows:
            break
        ___ row __ rows:
            yield row

def get_part_vendors():
    """ query part and vendor data from multiple tables"""
    conn _ None
    try:
        params _ config()
        conn _ psycopg2.c..(**params)
        cur _ conn.cursor()
        cur.e..("""
            SELECT part_name, vendor_name
            FROM parts
            INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
            INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
            ORDER BY part_name;
        """)
        ___ row __ iter_row(cur, 10):
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        __ conn is not None:
            conn.close()


__ __name__ == '__main__':
    get_part_vendors()