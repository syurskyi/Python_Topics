#!/usr/bin/python
_____ psycopg2
from config _____ config

def read_blob(part_id, path_to_dir):
    """ read BLOB data from a table """
    conn _ None
    try:
        # read database configuration
        params _ config()
        # connect to the PostgresQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor object
        cur _ conn.cursor()
        # execute the SELECT statement
        cur.e..(""" SELECT part_name, file_extension, drawing_data
                        FROM part_drawings
                        INNER JOIN parts on parts.part_id = part_drawings.part_id
                        WHERE parts.part_id = %s """,
                    (part_id,))

        blob _ cur.fetchone()
        open(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    read_blob(1, 'images/simtray.png')
    read_blob(2, 'images/speaker.png')