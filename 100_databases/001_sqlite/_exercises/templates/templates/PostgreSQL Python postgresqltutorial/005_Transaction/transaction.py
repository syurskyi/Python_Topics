#!/usr/bin/python
_____ ?
____ c.. _____ c..


___ add_part(part_name, vendor_list):
    # statement for inserting a new row into the parts table
    insert_part _ "I.. I.. parts(part_name) V..(%s) RETURNING part_id;"
    # statement for inserting a new row into the vendor_parts table
    assign_vendor _ "I.. I.. vendor_parts(vendor_id,part_id) V..(%s,%s)"

    conn _ w..
    ___
        params _ c..()
        conn _ ?.c..(**params)
        cur _ conn.c..
        # insert a new part
        cur.e..(insert_part, (part_name,))
        # get the part id
        part_id _ cur.f_o..[0]
        # assign parts provided by vendors
        ___ vendor_id __ vendor_list:
            cur.e..(assign_vendor, (vendor_id, part_id))

        # commit changes
        conn.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..


__ _____ __ ______
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Vibrator', (5, 6))
    add_part('Antenna', (6, 7))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))