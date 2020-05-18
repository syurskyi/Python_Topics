# _____ ?
# ____ ? _____ Er..
# ___
#    connection _ ?.c.. u.._"syurskyi"
#                                   p.._"1234"
#                                   h.._"127.0.0.1"
#                                   p.._"5432"
#                                   d.._"postgres_db"
#    ?.a_c__F..
#    cursor _ ?.c..
#    amount _ 2500
#
#    query _ """s.. balance f.. account w.. id = 624001562408"""
#    ?.e.. ?
#    record _ ?.f_o..  0
#    balance_account_A  _ in. ?
#    b.. -_ a..
#
#    # Withdraw from account A  now
#    sql_update_query _ """Update account set balance = @ w.. id = 624001562408"""
#    ?.e.. ? _A
#
#    query _ """s.. balance f.. account w.. id = 2236781258763"""
#    ?.e.. ?
#    record _ ?.f_o..  0
#    balance_account_B _ in. ?
#    b.. +_ a..
#
#    # Credit to  account B  now
#    sql_update_query _ """U.. account set balance = @ w.. id = 2236781258763"""
#    ?.e..? _B
#
#    # commiting both the transction to database
#    ?.c..
#    print("Transaction completed successfully ")
#
# ______  E.. ?.DE.. __ error
#     print ("Error in transction Reverting all other operations of a transction " ?
#     ?.r..
#
# f__
#     #closing database connection.
#     __(c..
#         ?.c..
#         ?.c..
#         print("PostgreSQL connection is closed")