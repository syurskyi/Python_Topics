_____ ?
____ ? _____ Er..

connection _ ?.c..(u.._"syurskyi",
                              p.._"1234",
                              h.._"127.0.0.1",
                              p.._"5432",
                              d.._"postgres_db")
w__ connection:
    w__ ?.c.. __ cursor:
        # Find item price
        query _ """s.. price f.. itemstable w.. itemid = 876"""
        cursor.e..(query)
        record _ ?.f_o..[0]
        Itemprice _ int(record)

        # find customer's ewallet balance
        query _ """s.. balance f.. ewallet w.. userId = 23"""
        ?.e..(query)
        record _ ?.f_o..[0]
        ewalletBalance _ int(record)
        new_EwalletBalance -_ Itemprice

        # Withdraw from ewallet now
        sql_update_query _ """Update ewallet set balance = %s w.. id = 23"""
        ?.e..(sql_update_query, (new_EwalletBalance,))

        # add to company's account
        query _ """s.. balance f.. account w.. accountId = 2236781258763"""
        ?.e..(query)
        record _ ?.f_o..
        accountBalance _ int(record)
        new_AccountBalance +_ Itemprice

        # Credit to  company account now
        sql_update_query _ """Update account set balance = %s w.. id = 2236781258763"""
        ?.e..(sql_update_query, (new_AccountBalance,))
        print("Transaction completed successfully ")