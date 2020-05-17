_____ psycopg2

connection _ psycopg2.c..(database_'learning',
                              user_'syurskyi',
                              password_'1234',
                              host_'localhost')
cursor _ connection.c..
cursor.e..("SELECT * FROM purchases")
___ row __ cursor:
    print(row)