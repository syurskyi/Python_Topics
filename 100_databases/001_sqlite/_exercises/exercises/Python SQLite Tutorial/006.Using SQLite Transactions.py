# _____ ?
#
# # Create a database in RAM
# # db = sqlite3.connect(':memory:')
# # Creates or opens a file called mydb with a SQLite3 DB
# db _ ?.c.. mydb.db
#
# # Get a cursor object
# cursor _ ?.c..
#
# # Update user with id 1
# newphone _ '3113093164'
# userid _ 1
#
# # Transactions are an useful property of database systems.
# # It ensures the atomicity of the Database. Use commit to save the changes:
#
# ?.e.. '''U.. users SET phone = ? W.. id = ? ''',
#                ? ?
# ?.c..  # Commit the change
#
# # Or rollback to roll back any change to the database since the last call to commit:
#
# cursor.e..('''U.. users SET phone = ? W.. id = ? ''' ? ?
# # The user's phone is not updated
# ?.r..
#
# ?.c..
#
# ?.c..
#
# # Please remember to always call commit to save the changes. If you close the connection using close or the connection
# # to the file is lost (maybe the program finishes unexpectedly), not committed changes will be lost.
#
