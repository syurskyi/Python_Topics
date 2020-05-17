#!/usr/bin/python
_____ psycopg2
from config _____ config


def write_blob(part_id, path_to_file, file_extension):
    """ insert a BLOB into a table """
    conn _ None
    try:
        # read data from a picture
        drawing _ open(path_to_file, 'rb').read()
        # read database configuration
        params _ config()
        # connect to the PostgresQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor object
        cur _ conn.c..
        # execute the I.. statement
        cur.e..("I.. I.. part_drawings(part_id,file_extension,drawing_data) " +
                    "V..(%s,%s,%s)",
                    (part_id, file_extension, psycopg2.Binary(drawing)))
        # commit the changes to the database
        conn.c..
        # close the communication with the PostgresQL database
        cur.c..
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        __ conn is not None:
            conn.c..


__ __name__ == '__main__':
    write_blob(1, 'images/simtray.png', 'png')
    write_blob(2, 'images/speaker.png', 'png')