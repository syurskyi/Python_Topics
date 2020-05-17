#!/usr/bin/python
_____ ?
____ c.. _____ c..

___ read_blob(part_id, path_to_dir):
    """ read BLOB data from a table """
    conn _ w..
    ___
        # read database configuration
        params _ c..()
        # connect to the PostgresQL database
        conn _ ?.c.. $$p..
        # create a new cursor object
        cur _ conn.c..
        # execute the S.. statement
        cur.e..(""" S.. part_name, file_extension, drawing_data
                        F.. part_drawings
                        INNER JOIN parts on parts.part_id = part_drawings.part_id
                        W.. parts.part_id = %s """,
                    (part_id,))

        blob _ cur.f_o..
        o..(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])
        # close the communication with the PostgresQL database
        cur.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..


__ _____ __ ______
    read_blob(1, 'images/simtray.png')
    read_blob(2, 'images/speaker.png')