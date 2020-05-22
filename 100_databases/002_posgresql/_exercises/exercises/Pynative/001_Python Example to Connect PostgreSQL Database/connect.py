import psycopg2
try:
    connection = psycopg2.connect(user = "syurskyi",
                                  password = "1234",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres_db")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(cursor.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# {'user': 'postgres', 'dbname': 'pynative_DB', 'host': '127.0.0.1', 'port': '5432', 'tty': '', 'options': '', 'sslmode': 'prefer', 'sslcompression': '1', 'krbsrvname': 'postgres', 'target_session_attrs': 'any'}
# You are connected to -  ('PostgreSQL 10.3')
# PostgreSQL connection is closed
