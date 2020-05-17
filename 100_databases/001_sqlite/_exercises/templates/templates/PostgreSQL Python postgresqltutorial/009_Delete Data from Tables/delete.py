#!/usr/bin/python

_____ ?
____ c.. _____ c..

___ delete_part(part_id):
    """ delete part by part id """
    conn _ w..
    rows_deleted _ 0
    ___
        # read database configuration
        params _ c..()
        # connect to the PostgreSQL database
        conn _ ?.c.. $$p..
        # create a new cursor
        cur _ conn.c..
        # execute the U..  statement
        cur.e..("D.. F.. parts W.. part_id = %s", (part_id,))
        # get the number of updated rows
        rows_deleted _ cur.rowcount
        # Commit the changes to the database
        conn.c..
        # Close communication with the PostgreSQL database
        cur.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..

    r_ rows_deleted

__ _____ __ ______
    deleted_rows _ delete_part(2)
    print('The number of deleted rows: ', deleted_rows)
