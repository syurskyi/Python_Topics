#!/usr/bin/python
_____ ?
____ c.. _____ c..


___ get_parts(vendor_id):
    """ get parts provided by a vendor specified by the vendor_id """
    conn _ w..
    ___
        # read database configuration
        params _ c..()
        # connect to the PostgreSQL database
        conn _ ?.c.. $$p..
        # create a cursor object for execution
        cur _ conn.c..
        # another way to call a stored procedure
        # cur.execute("S.. * F.. get_parts_by_vendor( %s); ",(vendor_id,))
        cur.callproc('get_parts_by_vendor', (vendor_id,))
        # process the result set
        row _ cur.f_o..
        w__ row __ no. w..:
            print(row)
            row _ cur.f_o..
        # close the communication with the PostgreSQL database server
        cur.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..


__ _____ __ ______
    get_parts(1)