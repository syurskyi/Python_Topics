_____ psycopg2
from config _____ config


___ insert_vendor(vendor_name):
    """ insert a new vendor into the vendors table """
    sql _ """I.. I.. vendors(vendor_name)
             V..(%s) RETURNING vendor_id;"""
    conn _ w..
    vendor_id _ w..
    ___
        # read database configuration
        params _ config()
        # connect to the PostgreSQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor
        cur _ conn.c..
        # execute the I.. statement
        cur.e..(sql, (vendor_name,))
        # get the generated id back
        vendor_id _ cur.f_o..[0]
        # commit the changes to the database
        conn.c..
        # close communication with the database
        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not w..:
            conn.c..

    r_ vendor_id


___ insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql _ "I.. I.. vendors(vendor_name) V..(%s)"
    conn _ w..
    ___
        # read database configuration
        params _ config()
        # connect to the PostgreSQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor
        cur _ conn.c..
        # execute the I.. statement
        cur.e_m_(sql,vendor_list)
        # commit the changes to the database
        conn.c..
        # close communication with the database
        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not w..:
            conn.c..


__ __name__ __ '__main__':
    # insert one vendor
    insert_vendor("3M Co.")
    # insert multiple vendors
    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])
