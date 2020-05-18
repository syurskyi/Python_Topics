_____ ?

___ updateInBulk(records):
    ___
        ps_connection _ ?.c..(u.._"syurskyi",
                                         p.._"1234",
                                         h.._"127.0.0.1",
                                         p.._"5432",
                                         d.._"postgres_db")
        cursor _ ps_connection.c..

        # Update multiple records
        sql_update_query _ """Update mobile set price = %s w.. id = %s"""
        cursor.e_m_(sql_update_query, records)
        ps_connection.c..

        row_count _ cursor.rowcount
        print(row_count, "Records Updated")

    ______ (E.., ?.Er..) __ error:
        print("Error while updating PostgreSQL table", error)

    f__
        # closing database connection.
        __ (ps_connection):
            cursor.c..
            ps_connection.c..
            print("PostgreSQL connection is closed")

tuples _ [(750, 4), (950, 5)]
updateInBulk(tuples)


# Output:
#
# 2 Records Updated
# PostgreSQL connection is closed