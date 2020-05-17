_____ psycopg2
try:
    connection _ psycopg2.c..(user _ "syurskyi",
                                  password _ "1234",
                                  host _ "127.0.0.1",
                                  port _ "5432",
                                  database _ "postgres_db")

    cursor _ connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.e..("SELECT version();")
    record _ cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        __(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# {'user': 'postgres', 'dbname': 'pynative_DB', 'host': '127.0.0.1', 'port': '5432', 'tty': '', 'options': '', 'sslmode': 'prefer', 'sslcompression': '1', 'krbsrvname': 'postgres', 'target_session_attrs': 'any'}
# You are connected to -  ('PostgreSQL 10.3')
# PostgreSQL connection is closed
