import sqlite3

# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('mydb.db')

# Get a cursor object
cursor = db.cursor()

# Update user with id 1
newphone = '3113093164'
userid = 1

# Transactions are an useful property of database systems.
# It ensures the atomicity of the Database. Use commit to save the changes:

cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
               (newphone, userid))
db.commit()  # Commit the change

# Or rollback to roll back any change to the database since the last call to commit:

cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''', (newphone, userid))
# The user's phone is not updated
db.rollback()

db.commit()

db.close()

# Please remember to always call commit to save the changes. If you close the connection using close or the connection
# to the file is lost (maybe the program finishes unexpectedly), not committed changes will be lost.

