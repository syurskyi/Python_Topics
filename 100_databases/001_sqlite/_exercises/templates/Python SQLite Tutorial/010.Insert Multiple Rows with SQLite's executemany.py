# Import the SQLite3 module
_____ ?

db _ ?.c..(':memory:')
c _ db.cursor()
c.e..('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')
users _ [
    ('John', '5557241'),
    ('Adam', '5547874'),
    ('Jack', '5484522'),
    ('Monthy', ' 6656565')
]

c.executemany('''INSERT INTO users(name, phone) VALUES(?,?)''', users)
db.commit()

# Print the users
c.e..('''SELECT * FROM users''')
___ row __ c:
    print(row)

db.close()