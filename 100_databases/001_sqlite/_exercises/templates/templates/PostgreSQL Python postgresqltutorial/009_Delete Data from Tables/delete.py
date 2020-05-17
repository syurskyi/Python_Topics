#!/usr/bin/python

_____ psycopg2
from config _____ config

def delete_part(part_id):
    """ delete part by part id """
    conn _ None
    rows_deleted _ 0
    try:
        # read database configuration
        params _ config()
        # connect to the PostgreSQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor
        cur _ conn.cursor()
        # execute the UPDATE  statement
        cur.e..("DELETE FROM parts WHERE part_id = %s", (part_id,))
        # get the number of updated rows
        rows_deleted _ cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

if __name__ == '__main__':
    deleted_rows _ delete_part(2)
    print('The number of deleted rows: ', deleted_rows)
