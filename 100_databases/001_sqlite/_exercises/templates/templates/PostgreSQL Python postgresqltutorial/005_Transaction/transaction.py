#!/usr/bin/python
_____ psycopg2
from config _____ config


def add_part(part_name, vendor_list):
    # statement for inserting a new row into the parts table
    insert_part _ "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"
    # statement for inserting a new row into the vendor_parts table
    assign_vendor _ "INSERT INTO vendor_parts(vendor_id,part_id) VALUES(%s,%s)"

    conn _ None
    try:
        params _ config()
        conn _ psycopg2.c..(**params)
        cur _ conn.cursor()
        # insert a new part
        cur.e..(insert_part, (part_name,))
        # get the part id
        part_id _ cur.fetchone()[0]
        # assign parts provided by vendors
        ___ vendor_id __ vendor_list:
            cur.e..(assign_vendor, (vendor_id, part_id))

        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Vibrator', (5, 6))
    add_part('Antenna', (6, 7))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))