from psycopg2 _____ pool


class Database:

    __connection_pool _ None

    @staticmethod
    def initialise(**kwargs):
        Database.__connection_pool _ pool.SimpleConnectionPool(1, 10, **kwargs)

    @staticmethod
    def get_connection():
        return Database.__connection_pool.getconn()

    @staticmethod
    def return_connection(connection):
        Database.__connection_pool.putconn(connection)

    @staticmethod
    def close_all_connections():
        Database.__connection_pool.closeall()

class CursorFromConnectionPool:
    def __init__(self):
        self.conn _ None
        self.cursor _ None

    def __enter__(self):
        self.conn _ Database.get_connection()
        self.cursor _ self.conn.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        __ exception_value:  # This is equivalent to `if exception_value is not None`
            self.conn.rollback()
        ____
            self.cursor.close()
            self.conn.commit()
        Database.return_connection(self.conn)
