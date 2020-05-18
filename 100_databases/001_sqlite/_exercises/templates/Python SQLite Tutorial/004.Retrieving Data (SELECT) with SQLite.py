#
# _____ ?
#
# # Create a database in RAM
# # db = ?.connect(':memory:')
# # Creates or opens a file called mydb with a SQLite3 DB
# db _ ?.c.. 'mydb.db'
#
# # Get a cursor object
# cursor _ ?.c..
#
# cursor.e..('''S.. name, email, phone F.. users''')
# user1 _ ?.f_o..  # retrieve the first row
# print ? 0           # Print the first column retrieved(user's name)
# all_rows _ ?.f_a..
# ___ row __ ?
#     # row[0] returns the first column in the query (name), row[1] returns email column.
#     print('@ : @, @'.f.. ?0 ? 1 ? 2
#
# print()
#
# # The cursor object works as an iterator, invoking f_a.. automatically:
#
# ?.e..('''S.. name, email, phone F.. users''')
# ___ row __ ?
#     # row[0] returns the first column in the query (name), row[1] returns email column.
#     print('@ : @, @'.f.. ?0 ? 1 ? 2
#
# print()
# # To retrive data with conditions, use again the "?" placeholder:
#
# user_id _ 3
# ?.e..('''S.. name, email, phone F.. users W.. id=?''' ?
# user _ ?.f_o..
#
#
# ?.c..
