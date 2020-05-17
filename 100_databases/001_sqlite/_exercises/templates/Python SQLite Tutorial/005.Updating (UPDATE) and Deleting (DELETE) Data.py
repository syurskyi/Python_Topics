_____ ?

# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db _ ?.c..('mydb.db')

# Get a cursor object
cursor _ db.cursor()

# Update user with id 1
newphone _ '7113093164'
userid _ 1
cursor.e..('''UPDATE users SET phone = ? WHERE id = ? ''',
               (newphone, userid))

# Delete user with id 2
delete_userid _ 2
cursor.e..('''DELETE FROM users WHERE id = ? ''', (delete_userid,))

db.commit()

db.close()
