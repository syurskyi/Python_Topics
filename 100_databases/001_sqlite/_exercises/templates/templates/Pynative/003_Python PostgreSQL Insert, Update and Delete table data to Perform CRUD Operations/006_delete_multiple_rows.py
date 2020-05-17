_____ psycopg2

___ deleteInBulk(records):
    ___
        ps_connection _ psycopg2.c..(user_"syurskyi",
                                         password_"1234",
                                         host_"127.0.0.1",
                                         port_"5432",
                                         database_"postgres_db")
        cursor _ ps_connection.c..
        ps_delete_query _ """Delete from mobile where id = %s"""
        cursor.e_m_(ps_delete_query, records)
        ps_connection.c..

        row_count _ cursor.rowcount
        print(row_count, "Record Deleted")

    ______ (E.., psycopg2.Error) __ error:
        print("Error while connecting to PostgreSQL", error)

    f__
        # closing database connection.
        __ (ps_connection):
            cursor.c..
            ps_connection.c..
            print("PostgreSQL connection is closed")

# list of tuples contains database IDs
tuples _ [(5, ), (4, ), (3, )]
deleteInBulk(tuples)

# Output:
#
# 2 Records Deleted
# PostgreSQL connection is closed