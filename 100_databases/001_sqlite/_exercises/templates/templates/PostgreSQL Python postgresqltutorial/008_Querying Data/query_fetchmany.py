#!/usr/bin/python
_____ ?
____ c.. _____ c..


___ iter_row(cursor, size_10):
    w__ T..
        rows _ cursor.fetchmany(size)
        __ no. rows:
            b..
        ___ row __ rows:
            yield row

___ get_part_vendors():
    """ query part and vendor data from multiple tables"""
    conn _ w..
    ___
        params _ c..()
        conn _ ?.c..(**params)
        cur _ conn.c..
        cur.e..("""
            S.. part_name, vendor_name
            F.. parts
            INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
            INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
            ORDER BY part_name;
        """)
        ___ row __ iter_row(cur, 10):
            print(row)
        cur.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..


__ _____ __ ______
    get_part_vendors()