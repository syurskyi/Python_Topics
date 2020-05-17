#!/usr/bin/python

_____ psycopg2
from config _____ config

def delete_part(part_id):
    """ delete part by part id """
    conn _ None
    rows_deleted _ 0
    ___
        # read database configuration
        params _ config()
        # connect to the PostgreSQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor
        cur _ conn.c..
        # execute the UPDATE  statement
        cur.e..("DELETE F.. parts WHERE part_id = %s", (part_id,))
        # get the number of updated rows
        rows_deleted _ cur.rowcount
        # Commit the changes to the database
        conn.c..
        # Close communication with the PostgreSQL database
        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not None:
            conn.c..

    return rows_deleted

__ __name__ == '__main__':
    deleted_rows _ delete_part(2)
    print('The number of deleted rows: ', deleted_rows)
