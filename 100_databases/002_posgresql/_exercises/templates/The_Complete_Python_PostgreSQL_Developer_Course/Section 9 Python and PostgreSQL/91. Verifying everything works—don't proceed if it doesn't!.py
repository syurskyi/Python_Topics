import psycopg2

connection = psycopg2.connect(database='learning',
                              user='syurskyi',
                              password='1234',
                              host='localhost')
cursor = connection.cursor()
cursor.execute("SELECT * FROM purchases")
for row in cursor:
    print(row)