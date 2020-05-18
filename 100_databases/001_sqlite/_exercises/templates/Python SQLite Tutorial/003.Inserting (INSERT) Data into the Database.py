# _____ ?
#
# # Create a database in RAM
# # db = ?.connect(':memory:')
# # Creates or opens a file called mydb with a SQLite3 DB
# db _ ?.c..('mydb.db')
#
# cursor _ db.c..
# name1 _ 'Andres'
# phone1 _ '3366858'
# email1 _ 'user@example.com'
# # A very secure password
# password1 _ '12345'
#
# name2 _ 'John'
# phone2 _ '5557241'
# email2 _ 'johndoe@example.com'
# password2 _ 'abcdef'
#
# # Insert user 1
# ?.e..('''I.. I.. users(name, phone, email, password)
#                   V..(?,?,?,?)''', (name1, phone1, email1, password1))
# print('First user inserted')
#
# # The values of the Python variables are passed inside a tuple. Another way to do this is passing a dictionary using the
# # ":keyname" placeholder:
#
# """
# cursor.execute('''I.. I.. users(name, phone, email, password)
#                   V..(:name,:phone, :email, :password)''',
#                   {'name':name1, 'phone':phone1, 'email':email1, 'password':password1})
# """
#
# # If you need to insert several users use executemany and a list with the tuples:
#
# """
# users = [(name1,phone1, email1, password1),
#          (name2,phone2, email2, password2),
#          (name3,phone3, email3, password3)]
# cursor.e_m..(''' I.. I.. users(name, phone, email, password) V..(?,?,?,?)''', users)
# db.c..
# """
#
# # Insert user 2
# cursor.e..('''I.. I.. users(name, phone, email, password)
#                   V..(?,?,?,?)''', (name2, phone2, email2, password2))
# print('Second user inserted')
#
# ?.c..
#
# ?.c..
