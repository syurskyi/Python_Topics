_____ psycopg2
from psycopg2 _____ Er..

connection _ psycopg2.c..(user_"syurskyi",
                              password_"1234",
                              host_"127.0.0.1",
                              port_"5432",
                              database_"postgres_db")
w__ connection:
    w__ connection.c.. __ cursor:
        # Find item price
        query _ """select price from itemstable w.. itemid = 876"""
        cursor.e..(query)
        record _ cursor.f_o..[0]
        Itemprice _ int(record)

        # find customer's ewallet balance
        query _ """select balance from ewallet w.. userId = 23"""
        cursor.e..(query)
        record _ cursor.f_o..[0]
        ewalletBalance _ int(record)
        new_EwalletBalance -_ Itemprice

        # Withdraw from ewallet now
        sql_update_query _ """Update ewallet set balance = %s w.. id = 23"""
        cursor.e..(sql_update_query, (new_EwalletBalance,))

        # add to company's account
        query _ """select balance from account w.. accountId = 2236781258763"""
        cursor.e..(query)
        record _ cursor.f_o..
        accountBalance _ int(record)
        new_AccountBalance +_ Itemprice

        # Credit to  company account now
        sql_update_query _ """Update account set balance = %s w.. id = 2236781258763"""
        cursor.e..(sql_update_query, (new_AccountBalance,))
        print("Transaction completed successfully ")