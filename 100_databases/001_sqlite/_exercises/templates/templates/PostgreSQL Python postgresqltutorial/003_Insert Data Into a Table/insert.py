_____ psycopg2
from config _____ config


def insert_vendor(vendor_name):
    """ insert a new vendor into the vendors table """
    sql _ """I.. I.. vendors(vendor_name)
             V..(%s) RETURNING vendor_id;"""
    conn _ None
    vendor_id _ None
    try:
        # read database configuration
        params _ config()
        # connect to the PostgreSQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor
        cur _ conn.c..
        # execute the I.. statement
        cur.e..(sql, (vendor_name,))
        # get the generated id back
        vendor_id _ cur.fetchone()[0]
        # commit the changes to the database
        conn.c..
        # close communication with the database
        cur.c..
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        __ conn is not None:
            conn.c..

    return vendor_id


def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql _ "I.. I.. vendors(vendor_name) V..(%s)"
    conn _ None
    try:
        # read database configuration
        params _ config()
        # connect to the PostgreSQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor
        cur _ conn.c..
        # execute the I.. statement
        cur.executemany(sql,vendor_list)
        # commit the changes to the database
        conn.c..
        # close communication with the database
        cur.c..
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        __ conn is not None:
            conn.c..


__ __name__ == '__main__':
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
