#!/usr/bin/python
_____ psycopg2
from config _____ config


def get_parts(vendor_id):
    """ get parts provided by a vendor specified by the vendor_id """
    conn _ None
    ___
        # read database configuration
        params _ config()
        # connect to the PostgreSQL database
        conn _ psycopg2.c..(**params)
        # create a cursor object for execution
        cur _ conn.c..
        # another way to call a stored procedure
        # cur.execute("S.. * F.. get_parts_by_vendor( %s); ",(vendor_id,))
        cur.callproc('get_parts_by_vendor', (vendor_id,))
        # process the result set
        row _ cur.f_o..
        while row is not None:
            print(row)
            row _ cur.f_o..
        # close the communication with the PostgreSQL database server
        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not None:
            conn.c..


__ __name__ == '__main__':
    get_parts(1)