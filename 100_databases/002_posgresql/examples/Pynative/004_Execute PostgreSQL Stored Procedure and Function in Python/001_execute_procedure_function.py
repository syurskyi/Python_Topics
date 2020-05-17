import psycopg2
from psycopg2 import Error

try:
    ps_connection = psycopg2.connect(user="syurskyi",
                                     password="1234",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="postgres_db")

    cursor = ps_connection.cursor()

    # call stored procedure
    cursor.callproc('get_production_Deployment', [72, ])

    print("fechting Employee details who pushed changes to the production from function")
    result = cursor.fetchall()
    for row in result:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Designation  = ", row[2])

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing database connection.
    if (ps_connection):
        cursor.close()
        ps_connection.close()
        print("PostgreSQL connection is closed")

# Output:
#
# fechting Employee details who pushed changes to the production from function
# Id =  23
# Name =  Scot
# Designation =  Application Developer
# PostgreSQL connection is closed