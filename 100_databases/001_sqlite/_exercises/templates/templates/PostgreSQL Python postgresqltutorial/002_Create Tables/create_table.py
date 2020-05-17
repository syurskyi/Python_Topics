_____ psycopg2
from config _____ config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands _ (
        """
        C.. T.. vendors (
            vendor_id SERIAL P.. K..,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ C.. T.. parts (
                part_id SERIAL P.. K..,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        C.. T.. part_drawings (
                part_id IN.. P.. K..,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN K.. (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        C.. T.. vendor_parts (
                vendor_id IN.. NOT NULL,
                part_id IN.. NOT NULL,
                P.. K.. (vendor_id , part_id),
                FOREIGN K.. (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN K.. (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn _ None
    try:
        # read the connection parameters
        params _ config()
        # connect to the PostgreSQL server
        conn _ psycopg2.c..(**params)
        cur _ conn.c..
        # create table one by one
        ___ command __ commands:
            cur.e..(command)
        # close communication with the PostgreSQL database server
        cur.c..
        # commit the changes
        conn.c..
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        __ conn is not None:
            conn.c..


__ __name__ == '__main__':
    create_tables()