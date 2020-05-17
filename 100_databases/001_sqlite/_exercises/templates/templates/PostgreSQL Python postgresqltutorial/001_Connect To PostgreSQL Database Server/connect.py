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
        cur _ conn.c..

        # execute a statement
        print('PostgreSQL database version:')
        cur.e..('S.. version()')

        # display the PostgreSQL database server version
        db_version _ cur.f_o..
        print(db_version)

        # close the communication with the PostgreSQL
        cur.c..
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        __ conn is not None:
            conn.c..
            print('Database connection closed.')


__ __name__ == '__main__':
    c..()