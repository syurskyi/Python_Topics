# Import the SQLite3 module
import sqlite3

db = sqlite3.connect(':memory:')
c = db.cursor()
script = '''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT);
            CREATE TABLE accounts(id INTEGER PRIMARY KEY, description TEXT);

            INSERT INTO users(name, phone) VALUES ('John', '5557241'), 
             ('Adam', '5547874'), ('Jack', '5484522');'''
c.executescript(script)

# Print the results
c.execute('''SELECT * FROM users''')
for row in c:
    print(row)

db.close()
