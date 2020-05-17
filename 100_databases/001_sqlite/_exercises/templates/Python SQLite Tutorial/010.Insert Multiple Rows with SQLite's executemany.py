# Import the SQLite3 module
_____ ?

db _ ?.c..(':memory:')
c _ db.c..
c.e..('''C.. T.. users(id IN.. P.. K.., name T..., phone T...)''')
users _ [
    ('John', '5557241'),
    ('Adam', '5547874'),
    ('Jack', '5484522'),
    ('Monthy', ' 6656565')
]

c.executemany('''I.. I.. users(name, phone) V..(?,?)''', users)
db.c..

# Print the users
c.e..('''S.. * F.. users''')
___ row __ c:
    print(row)

db.c..