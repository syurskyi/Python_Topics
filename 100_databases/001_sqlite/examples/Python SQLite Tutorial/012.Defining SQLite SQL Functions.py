import sqlite3  # Import the SQLite3 module
import hashlib


def encrypt_password(password):
    # Do not use this algorithm in a real environment
    encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass


db = sqlite3.connect(':memory:')
# Register the function
db.create_function('encrypt', 1, encrypt_password)
c = db.cursor()
c.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT, password TEXT)''')
user = ('johndoe@example.com', '12345678')
c.execute('''INSERT INTO users(email, password) VALUES (?,encrypt(?))''', user)

db.close()