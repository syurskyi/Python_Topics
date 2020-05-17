#!/usr/bin/python
_____ ?
____ c.. _____ c..


___ write_blob(part_id, path_to_file, file_extension):
    """ insert a BLOB into a table """
    conn _ w..
    ___
        # read data from a picture
        drawing _ o..(path_to_file, 'rb').r..
        # read database configuration
        params _ c..()
        # connect to the PostgresQL database
        conn _ ?.c.. $$p..
        # create a new cursor object
        cur _ conn.c..
        # execute the I.. statement
        cur.e..("I.. I.. part_drawings(part_id,file_extension,drawing_data) " +
                    "V..(%s,%s,%s)",
                    (part_id, file_extension, ?.Binary(drawing)))
        # commit the changes to the database
        conn.c..
        # close the communication with the PostgresQL database
        cur.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..


__ _____ __ ______
    write_blob(1, 'images/simtray.png', 'png')
    write_blob(2, 'images/speaker.png', 'png')