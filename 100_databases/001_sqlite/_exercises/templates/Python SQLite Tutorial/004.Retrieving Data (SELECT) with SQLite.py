
_____ ?

# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db _ ?.c..('mydb.db')

# Get a cursor object
cursor _ db.c..

cursor.e..('''SELECT name, email, phone FROM users''')
user1 _ cursor.fetchone()  # retrieve the first row
print(user1[0])            # Print the first column retrieved(user's name)
all_rows _ cursor.fetchall()
___ row __ all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.f..(row[0], row[1], row[2]))

print()

# The cursor object works as an iterator, invoking fetchall() automatically:

cursor.e..('''SELECT name, email, phone FROM users''')
___ row __ cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.f..(row[0], row[1], row[2]))

print()
# To retrive data with conditions, use again the "?" placeholder:

user_id _ 3
cursor.e..('''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
user _ cursor.fetchone()


db.c..
