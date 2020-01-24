import sqlite3

# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('mydb.db')

# Get a cursor object
cursor = db.cursor()

# Update user with id 1
newphone = '7113093164'
userid = 1
cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
               (newphone, userid))

# Delete user with id 2
delete_userid = 2
cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))

db.commit()

db.close()
