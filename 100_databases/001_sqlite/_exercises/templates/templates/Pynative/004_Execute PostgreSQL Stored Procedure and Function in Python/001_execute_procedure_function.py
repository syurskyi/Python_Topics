_____ ?
____ ? _____ Er..

___
    ps_connection _ ?.c..(u.._"syurskyi",
                                     p.._"1234",
                                     h.._"127.0.0.1",
                                     p.._"5432",
                                     d.._"postgres_db")

    cursor _ ps_connection.c..

    # call stored procedure
    ?.callproc('get_production_Deployment', [72, ])

    print("fechting Employee details who pushed changes to the production f.. function")
    result _ ?.f_a..
    ___ row __ result:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Designation  = ", row[2])

______ (E.., ?.DE..) __ error:
    print("Error while connecting to PostgreSQL", error)

f__
    # closing database connection.
    __ (ps_connection):
        ?.c..
        ps_connection.c..
        print("PostgreSQL connection is closed")

# Output:
#
# fechting Employee details who pushed changes to the production from function
# Id =  23
# Name =  Scot
# Designation =  Application Developer
# PostgreSQL connection is closed