
import sqlite3

# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('mydb.db')

# Get a cursor object
cursor = db.cursor()

cursor.execute('''SELECT name, email, phone FROM users''')
user1 = cursor.fetchone()  # retrieve the first row
print(user1[0])            # Print the first column retrieved(user's name)
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

print()

# The cursor object works as an iterator, invoking fetchall() automatically:

cursor.execute('''SELECT name, email, phone FROM users''')
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

print()
# To retrive data with conditions, use again the "?" placeholder:

user_id = 3
cursor.execute('''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
user = cursor.fetchone()


db.close()
