# _____ ?  #Import the SQLite3 module
# ___
#     # Creates or opens a file called mydb with a SQLite3 DB
#     db _ ?.c..('mydb.db')
#     # Get a cursor object
#     cursor _ db.c..
#     # Check if table users does not exist and create it
#     ?.e.. '''C.. T.. I. N.. E..
#                       users(id IN.. P.. K.., name T..., phone T..., email T... unique, password T...)''')
#     # Commit the change
#     ?.c..
# # Catch the exceptio
# ______ E.. __ e
#     # Roll back any change if something goes wrong
#     ?.r..
#     r_ ?
# f__
#     # Close the db connection
#     ?.c..
#
# # We can use the Connection object as context manager to automatically commit or rollback transactions:
#
