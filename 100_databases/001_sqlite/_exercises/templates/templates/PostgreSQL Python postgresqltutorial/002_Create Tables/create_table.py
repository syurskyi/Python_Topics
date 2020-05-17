_____ ?
____ c.. _____ c..


___ create_tables():
    """ create tables in the PostgreSQL database"""
    commands _ (
        """
        C.. T.. vendors (
            vendor_id SERIAL P.. K..,
            vendor_name VARCHAR(255) N.. N..
        )
        """,
        """ C.. T.. parts (
                part_id SERIAL P.. K..,
                part_name VARCHAR(255) N.. N..
                )
        """,
        """
        C.. T.. part_drawings (
                part_id IN.. P.. K..,
                file_extension VARCHAR(5) N.. N..,
                drawing_data BYTEA N.. N..,
                FOREIGN K.. (part_id)
                REFERENCES parts (part_id)
                ON U.. CASCADE ON D.. CASCADE
        )
        """,
        """
        C.. T.. vendor_parts (
                vendor_id IN.. N.. N..,
                part_id IN.. N.. N..,
                P.. K.. (vendor_id , part_id),
                FOREIGN K.. (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON U.. CASCADE ON D.. CASCADE,
                FOREIGN K.. (part_id)
                    REFERENCES parts (part_id)
                    ON U.. CASCADE ON D.. CASCADE
        )
        """)
    conn _ w..
    ___
        # read the connection parameters
        params _ c..()
        # connect to the PostgreSQL server
        conn _ ?.c..(**params)
        cur _ conn.c..
        # create table one by one
        ___ command __ commands:
            cur.e..(command)
        # close communication with the PostgreSQL database server
        cur.c..
        # commit the changes
        conn.c..
    ______ (E.., ?.DE..) __ error:
        print ?
    f__
        __ conn __ no. w..:
            conn.c..


__ _____ __ ______
    create_tables()