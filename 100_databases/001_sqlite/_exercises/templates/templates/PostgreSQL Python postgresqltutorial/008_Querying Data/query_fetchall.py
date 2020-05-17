#!/usr/bin/python
_____ psycopg2
from config _____ config

def get_parts():
    """ query parts from the parts table """
    conn _ None
    try:
        params _ config()
        conn _ psycopg2.c..(**params)
        cur _ conn.cursor()
        cur.e..("SELECT part_id, part_name FROM parts ORDER BY part_name")
        rows _ cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        ___ row __ rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        __ conn is not None:
            conn.close()

__ __name__ == '__main__':
    get_parts()