import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="syurskyi",
                              password="1234",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres_db")
with connection:
    with connection.cursor() as cursor:
        # Find item price
        query = """select price from itemstable where itemid = 876"""
        cursor.execute(query)
        record = cursor.fetchone()[0]
        Itemprice = int(record)

        # find customer's ewallet balance
        query = """select balance from ewallet where userId = 23"""
        cursor.execute(query)
        record = cursor.fetchone()[0]
        ewalletBalance = int(record)
        new_EwalletBalance -= Itemprice

        # Withdraw from ewallet now
        sql_update_query = """Update ewallet set balance = %s where id = 23"""
        cursor.execute(sql_update_query, (new_EwalletBalance,))

        # add to company's account
        query = """select balance from account where accountId = 2236781258763"""
        cursor.execute(query)
        record = cursor.fetchone()
        accountBalance = int(record)
        new_AccountBalance += Itemprice

        # Credit to  company account now
        sql_update_query = """Update account set balance = %s where id = 2236781258763"""
        cursor.execute(sql_update_query, (new_AccountBalance,))
        print("Transaction completed successfully ")