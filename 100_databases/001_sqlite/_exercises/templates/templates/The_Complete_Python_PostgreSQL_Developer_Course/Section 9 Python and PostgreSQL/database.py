from psycopg2 _____ pool


class Database:

    __connection_pool _ None

    @staticmethod
    ___ initialise(**kwargs):
        Database.__connection_pool _ pool.SimpleConnectionPool(1, 10, **kwargs)

    @staticmethod
    ___ get_connection():
        r_ Database.__connection_pool.getconn()

    @staticmethod
    ___ return_connection(connection):
        Database.__connection_pool.putconn(connection)

    @staticmethod
    ___ close_all_connections():
        Database.__connection_pool.closeall()

class CursorFromConnectionPool:
    ___ __init__(self):
        self.conn _ None
        self.cursor _ None

    ___ __enter__(self):
        self.conn _ Database.get_connection()
        self.cursor _ self.conn.c..
        r_ self.cursor

    ___ __exit__(self, exception_type, exception_value, exception_traceback):
        __ exception_value:  # This is equivalent to `if exception_value is not None`
            self.conn.rollback()
        ____
            self.cursor.c..
            self.conn.c..
        Database.return_connection(self.conn)
