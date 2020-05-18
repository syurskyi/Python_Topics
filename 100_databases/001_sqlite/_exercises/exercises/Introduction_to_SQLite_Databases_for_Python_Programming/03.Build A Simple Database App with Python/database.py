# ______ _3
#
#
# # Query The DB and Return All Records
#
# ___ show_all
#     # connect to database
#     conn _ _3.c.. customer.db
#
#     # Create a cursor
#     c _ ?.c..
#
#     # Query The Database
#     ?.e.. S.. r.., _ F.. customers
#
#     items _ c.f..
#
#     ___ item __ ?
#         print ?
#
#     # Commit our command
#     ?.c..
#
#     # Close our connection
#     ?.c..
#
#
# # Add a New Record to the Table
# ___ add_one first last email
#     conn _ _3.c.. customer.db
#     c _ ?.c..
#     c.e.. I.. I.. customers V... |?, ?, ? *, ?  ?  ?
#     ?.c..
#     ?.c..
#
#
# # Add Many Records to Table
# ___ add_many li..
#     conn _ _3.c.. customer.db
#     c _ ?.c..
#     c.e..m.. I.. I.. customers V.. |?, ?, ?|  ?
#     ?.c..
#     ?.c..
#
#
# # Delete Record from the table
# ___ delete_one id
#     conn _ _3.c.. customer.db
#     c _ ?.c..
#     c.e..  D.. f.. customers W.. r.. _ ? , ?
#     ?.c..
#     ?.c..
#
#
# # Lookup with Where
# ___ email_lookup email
#     conn _ _3.c.. customer.db
#     c _ ?.c..
#     c.e.. S.. _ from customers W.. email _ ? , ?
#     items _ c.f..
#     ___ item __ ?
#         print ?
#     ?.c..
#     ?.c..
