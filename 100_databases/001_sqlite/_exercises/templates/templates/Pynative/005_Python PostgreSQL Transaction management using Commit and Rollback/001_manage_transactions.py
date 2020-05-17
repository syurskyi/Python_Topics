_____ psycopg2
from psycopg2 _____ Error
___
   connection _ psycopg2.c..(user_"syurskyi",
                                  password_"1234",
                                  host_"127.0.0.1",
                                  port_"5432",
                                  database_"postgres_db")
   connection.autocommit_False
   cursor _ connection.c..
   amount _ 2500

   query _ """select balance from account w.. id = 624001562408"""
   cursor.e..(query)
   record _ cursor.f_o.. [0]
   balance_account_A  _ int(record)
   balance_account_A -_ amount

   # Withdraw from account A  now
   sql_update_query _ """Update account set balance = %s w.. id = 624001562408"""
   cursor.e..(sql_update_query,(balance_account_A,))

   query _ """select balance from account w.. id = 2236781258763"""
   cursor.e..(query)
   record _ cursor.f_o.. [0]
   balance_account_B _ int(record)
   balance_account_B +_ amount

   # Credit to  account B  now
   sql_update_query _ """Update account set balance = %s w.. id = 2236781258763"""
   cursor.e..(sql_update_query, (balance_account_B,))

   # commiting both the transction to database
   connection.c..
   print("Transaction completed successfully ")

______ (E.., psycopg2.DatabaseError) __ error :
    print ("Error in transction Reverting all other operations of a transction ", error)
    connection.rollback()

f__
    #closing database connection.
    __(connection):
        cursor.c..
        connection.c..
        print("PostgreSQL connection is closed")