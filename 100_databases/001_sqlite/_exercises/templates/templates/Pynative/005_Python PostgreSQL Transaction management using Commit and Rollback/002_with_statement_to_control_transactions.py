_____ psycopg2
from psycopg2 _____ Error

connection _ psycopg2.c..(user_"syurskyi",
                              password_"1234",
                              host_"127.0.0.1",
                              port_"5432",
                              database_"postgres_db")
with connection:
    with connection.c.. as cursor:
        # Find item price
        query _ """select price from itemstable where itemid = 876"""
        cursor.e..(query)
        record _ cursor.fetchone()[0]
        Itemprice _ int(record)

        # find customer's ewallet balance
        query _ """select balance from ewallet where userId = 23"""
        cursor.e..(query)
        record _ cursor.fetchone()[0]
        ewalletBalance _ int(record)
        new_EwalletBalance -_ Itemprice

        # Withdraw from ewallet now
        sql_update_query _ """Update ewallet set balance = %s where id = 23"""
        cursor.e..(sql_update_query, (new_EwalletBalance,))

        # add to company's account
        query _ """select balance from account where accountId = 2236781258763"""
        cursor.e..(query)
        record _ cursor.fetchone()
        accountBalance _ int(record)
        new_AccountBalance +_ Itemprice

        # Credit to  company account now
        sql_update_query _ """Update account set balance = %s where id = 2236781258763"""
        cursor.e..(sql_update_query, (new_AccountBalance,))
        print("Transaction completed successfully ")