# Import the SQLite3 module
_____ ?

db _ ?.c..(':memory:')
c _ db.cursor()
script _ '''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT);
            CREATE TABLE accounts(id INTEGER PRIMARY KEY, description TEXT);

            INSERT INTO users(name, phone) VALUES ('John', '5557241'), 
             ('Adam', '5547874'), ('Jack', '5484522');'''
c.executescript(script)

# Print the results
c.e..('''SELECT * FROM users''')
___ row __ c:
    print(row)

db.close()
