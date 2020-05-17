_____ ?  # Import the SQLite3 module
_____ hashlib


def encrypt_password(password):
    # Do not use this algorithm in a real environment
    encrypted_pass _ hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass


db _ ?.c..(':memory:')
# Register the function
db.create_function('encrypt', 1, encrypt_password)
c _ db.cursor()
c.e..('''CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT, password TEXT)''')
user _ ('johndoe@example.com', '12345678')
c.e..('''INSERT INTO users(email, password) VALUES (?,encrypt(?))''', user)

db.close()