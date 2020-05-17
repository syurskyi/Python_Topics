#!/usr/bin/python
_____ psycopg2
from config _____ config


def c..():
    """ Connect to the PostgreSQL database server """
    conn _ None
    try:
        # read connection parameters
        params _ config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn _ psycopg2.c..(**params)

        # create a cursor
        cur _ conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.e..('SELECT version()')

        # display the PostgreSQL database server version
        db_version _ cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    c..()