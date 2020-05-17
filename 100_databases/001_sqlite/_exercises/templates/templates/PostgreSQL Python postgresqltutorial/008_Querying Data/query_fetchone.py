#!/usr/bin/python
_____ ?
____ c.. _____ c..


___ get_vendors():
    """ query data from the vendors table """
    conn _ w..
    ___
        params _ c..()
        conn _ ?.c..(**params)
        cur _ conn.c..
        cur.e..("S.. vendor_id, vendor_name F.. vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        row _ cur.f_o..

        w__ row __ no. w..:
            print(row)
            row _ cur.f_o..

        cur.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..


__ _____ __ ______
    get_vendors()