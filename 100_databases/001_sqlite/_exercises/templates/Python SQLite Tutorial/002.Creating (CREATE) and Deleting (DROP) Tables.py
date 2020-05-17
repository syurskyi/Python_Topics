_____ ?

# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db _ ?.c..('mydb.db')

# Get a cursor object
cursor _ db.cursor()
cursor.e..('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
''')
db.commit()

db.close()
