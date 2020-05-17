_____ ?  # Import the SQLite3 module
_____ hashlib


def encrypt_password(password):
    # Do not use this algorithm in a real environment
    encrypted_pass _ hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass


db _ ?.c..(':memory:')
# Register the function
db.create_function('encrypt', 1, encrypt_password)
c _ db.c..
c.e..('''C.. T.. users(id IN.. P.. K.., email T..., password T...)''')
user _ ('johndoe@example.com', '12345678')
c.e..('''I.. I.. users(email, password) V.. (?,encrypt(?))''', user)

db.c..