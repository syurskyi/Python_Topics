_____ ?
____ ? _____ Er..
___
   connection _ ?.c..(u.._"syurskyi",
                                  p.._"1234",
                                  h.._"127.0.0.1",
                                  p.._"5432",
                                  d.._"postgres_db")
   ?.autocommit_False
   cursor _ ?.c..
   amount _ 2500

   query _ """s.. balance f.. account w.. id = 624001562408"""
   ?.e..(query)
   record _ ?.f_o.. [0]
   balance_account_A  _ int(record)
   balance_account_A -_ amount

   # Withdraw from account A  now
   sql_update_query _ """Update account set balance = %s w.. id = 624001562408"""
   ?.e..(sql_update_query,(balance_account_A,))

   query _ """s.. balance f.. account w.. id = 2236781258763"""
   ?.e..(query)
   record _ ?.f_o.. [0]
   balance_account_B _ int(record)
   balance_account_B +_ amount

   # Credit to  account B  now
   sql_update_query _ """Update account set balance = %s w.. id = 2236781258763"""
   ?.e..(sql_update_query, (balance_account_B,))

   # commiting both the transction to database
   ?.c..
   print("Transaction completed successfully ")

______ (E.., ?.DE..) __ error :
    print ("Error in transction Reverting all other operations of a transction ", error)
    ?.r..

f__
    #closing database connection.
    __(connection):
        ?.c..
        ?.c..
        print("PostgreSQL connection is closed")