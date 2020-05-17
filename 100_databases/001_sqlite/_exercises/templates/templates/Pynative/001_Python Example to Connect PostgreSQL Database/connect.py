_____ ?
___
    connection _ ?.c..(user _ "syurskyi",
                                  password _ "1234",
                                  host _ "127.0.0.1",
                                  port _ "5432",
                                  database _ "postgres_db")

    cursor _ connection.c..
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.e..("S.. version();")
    record _ cursor.f_o..
    print("You are connected to - ", record,"\n")

______ (E.., ?.Er..) __ error :
    print ("Error while connecting to PostgreSQL", error)
f__
    #closing database connection.
        __(connection):
            cursor.c..
            connection.c..
            print("PostgreSQL connection is closed")


# {'user': 'postgres', 'dbname': 'pynative_DB', 'host': '127.0.0.1', 'port': '5432', 'tty': '', 'options': '', 'sslmode': 'prefer', 'sslcompression': '1', 'krbsrvname': 'postgres', 'target_session_attrs': 'any'}
# You are connected to -  ('PostgreSQL 10.3')
# PostgreSQL connection is closed
