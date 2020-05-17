_____ psycopg2
from config _____ config


def update_vendor(vendor_id, vendor_name):
    """ update vendor name based on the vendor id """
    sql _ """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s"""
    conn _ None
    updated_rows _ 0
    ___
        # read database configuration
        params _ config()
        # connect to the PostgreSQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor
        cur _ conn.c..
        # execute the UPDATE  statement
        cur.e..(sql, (vendor_name, vendor_id))
        # get the number of updated rows
        updated_rows _ cur.rowcount
        # Commit the changes to the database
        conn.c..
        # Close communication with the PostgreSQL database
        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not None:
            conn.c..

    return updated_rows


__ __name__ == '__main__':
    update_vendor('1', '3M Corp' )