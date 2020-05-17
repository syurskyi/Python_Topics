import psycopg2
from psycopg2 import Error
try:
   connection = psycopg2.connect(user="syurskyi",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
   connection.autocommit=False
   cursor = connection.cursor()
   amount = 2500

   query = """select balance from account where id = 624001562408"""
   cursor.execute(query)
   record = cursor.fetchone() [0]
   balance_account_A  = int(record)
   balance_account_A -= amount

   # Withdraw from account A  now
   sql_update_query = """Update account set balance = %s where id = 624001562408"""
   cursor.execute(sql_update_query,(balance_account_A,))

   query = """select balance from account where id = 2236781258763"""
   cursor.execute(query)
   record = cursor.fetchone() [0]
   balance_account_B = int(record)
   balance_account_B += amount

   # Credit to  account B  now
   sql_update_query = """Update account set balance = %s where id = 2236781258763"""
   cursor.execute(sql_update_query, (balance_account_B,))

   # commiting both the transction to database
   connection.commit()
   print("Transaction completed successfully ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error in transction Reverting all other operations of a transction ", error)
    connection.rollback()

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")