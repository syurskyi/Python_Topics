_____ ?

___ deleteInBulk(records):
    ___
        ps_connection _ ?.c..(u.._"syurskyi",
                                         p.._"1234",
                                         h.._"127.0.0.1",
                                         p.._"5432",
                                         d.._"postgres_db")
        cursor _ ps_connection.c..
        ps_delete_query _ """D.. f.. mobile w.. id = %s"""
        ?.e_m_(ps_delete_query, records)
        ps_connection.c..

        row_count _ ?.r..
        print(row_count, "Record Deleted")

    ______ (E.., ?.Er..) __ error:
        print("Error while connecting to PostgreSQL", error)

    f__
        # closing database connection.
        __ (ps_connection):
            ?.c..
            ps_connection.c..
            print("PostgreSQL connection is closed")

# list of tuples contains database IDs
tuples _ [(5, ), (4, ), (3, )]
deleteInBulk(tuples)

# Output:
#
# 2 Records Deleted
# PostgreSQL connection is closed