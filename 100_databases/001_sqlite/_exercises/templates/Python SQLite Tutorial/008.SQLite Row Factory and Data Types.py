_____ ?

db _ ?.c..('mydb.db')
db.r_f.. _ ?.Row
cursor _ db.c..
cursor.e..('''S.. name, email, phone F.. users''')
___ row __ cursor:
    # row['name'] returns the name column in the query, row['email'] returns email column.
    print('@ : @, @'.f..(row['name'], row['email'], row['phone']))
db.c..

