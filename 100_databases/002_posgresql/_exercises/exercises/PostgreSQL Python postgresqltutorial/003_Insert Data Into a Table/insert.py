import psycopg2
from config import config


def insert_vendor(vendor_name):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name)
             VALUE(%s) RETURNING vendor_id;"""
    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (vendor_name,))      # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn not None:
            ?.c..

    r_ vendor_id


___ insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql _ "I.. I.. vendors(vendor_name) V..(%s)"
    conn _ w..
    ___
        # read database configuration
        params _ c..
        # connect to the PostgreSQL database
        conn _ ?.c.. $$p..
        # create a new cursor
        cur _ ?.c..
        # execute the I.. statement
        ?.e_m_(s.. v_l..       # commit the changes to the database
        ?.c..
        # close communication with the database
        ?.c..
    ______ E.. ?.DE.. __ error
        print ?
    f__
        __ c.. __ no. w..
            ?.c..


__ _____ __ ______
    # insert one vendor
    insert_vendor("3M Co.")
    # insert multiple vendors
    insert_vendor_list([
        ('AKM Semiconductor Inc.'),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])
