#!/usr/bin/python

_____ psycopg2
from config _____ config

___ delete_part(part_id):
    """ delete part by part id """
    conn _ w..
    rows_deleted _ 0
    ___
        # read database configuration
        params _ config()
        # connect to the PostgreSQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor
        cur _ conn.c..
        # execute the U..  statement
        cur.e..("D.. F.. parts WHERE part_id = %s", (part_id,))
        # get the number of updated rows
        rows_deleted _ cur.rowcount
        # Commit the changes to the database
        conn.c..
        # Close communication with the PostgreSQL database
        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not w..:
            conn.c..

    r_ rows_deleted

__ __name__ __ '__main__':
    deleted_rows _ delete_part(2)
    print('The number of deleted rows: ', deleted_rows)
