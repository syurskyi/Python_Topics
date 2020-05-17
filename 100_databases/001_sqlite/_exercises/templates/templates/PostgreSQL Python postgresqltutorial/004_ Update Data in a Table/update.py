_____ ?
____ c.. _____ c..


___ update_vendor(vendor_id, vendor_name):
    """ update vendor name based on the vendor id """
    sql _ """ U.. vendors
                SET vendor_name = %s
                W.. vendor_id = %s"""
    conn _ w..
    updated_rows _ 0
    ___
        # read database configuration
        params _ c..()
        # connect to the PostgreSQL database
        conn _ ?.c.. $$p..
        # create a new cursor
        cur _ conn.c..
        # execute the U..  statement
        cur.e..(sql, (vendor_name, vendor_id))
        # get the number of updated rows
        updated_rows _ cur.rowcount
        # Commit the changes to the database
        conn.c..
        # Close communication with the PostgreSQL database
        cur.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..

    r_ updated_rows


__ _____ __ ______
    update_vendor('1', '3M Corp' )