#!/usr/bin/python
_____ ?
____ c.. _____ c..

___ get_parts():
    """ query parts from the parts table """
    conn _ w..
    ___
        params _ c..()
        conn _ ?.c.. $$p..
        cur _ conn.c..
        cur.e..("S.. part_id, part_name F.. parts ORDER BY part_name")
        rows _ cur.f_a..
        print("The number of parts: ", cur.rowcount)
        ___ row __ rows:
            print(row)
        cur.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..

__ _____ __ ______
    get_parts()