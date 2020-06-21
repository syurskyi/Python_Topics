# _____ ?
# ____ ? _____ Er..
#
# connection _ ?.c.. u.._"syurskyi"
#                               p.._"1234"
#                               h.._"127.0.0.1"
#                               p.._"5432"
#                               d.._"postgres_db"
# w__ ?
#     w__ ?.c.. __ cursor
#         # Find item price
#         query _ """s.. price f.. itemstable w.. itemid = 876"""
#         ?.e.. ?
#         record _ ?.f_o.. 0
#         Itemprice _ in. ?
#
#         # find customer's ewallet balance
#         query _ """s.. balance f.. ewallet w.. userId = 23"""
#         ?.e.. ?
#         record _ ?.f_o.. 0
#         ewalletBalance _ in. ?
#         new_EwalletBalance -_ Itemprice
#
#         # Withdraw from ewallet now
#         sql_update_query _ """Update ewallet set balance = @ w.. id = 23"""
#         ?.e.. ? n..
#
#         # add to company's account
#         query _ """s.. balance f.. account w.. accountId = 2236781258763"""
#         ?.e.. ?
#         record _ ?.f_o..
#         accountBalance _ in. ?
#         new_AccountBalance +_ Itemprice
#
#         # Credit to  company account now
#         sql_update_query _ """Update account set balance = @ w.. id = 2236781258763"""
#         ?.e.. ? n..
#         print("Transaction completed successfully ")