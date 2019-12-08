# Import the SQLite3 module
import sqlite3

db = sqlite3.connect(':memory:')
c = db.cursor()
c.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')
users = [
    ('John', '5557241'),
    ('Adam', '5547874'),
    ('Jack', '5484522'),
    ('Monthy', ' 6656565')
]

c.executemany('''INSERT INTO users(name, phone) VALUES(?,?)''', users)
db.commit()

# Print the users
c.execute('''SELECT * FROM users''')
for row in c:
    print(row)

db.close()