_____ ?

# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db _ ?.c..('mydb.db')

# Get a cursor object
cursor _ db.c..

# Update user with id 1
newphone _ '7113093164'
userid _ 1
cursor.e..('''U.. users SET phone = ? W.. id = ? ''',
               (newphone, userid))

# Delete user with id 2
delete_userid _ 2
cursor.e..('''D.. F.. users W.. id = ? ''', (delete_userid,))

db.c..

db.c..
