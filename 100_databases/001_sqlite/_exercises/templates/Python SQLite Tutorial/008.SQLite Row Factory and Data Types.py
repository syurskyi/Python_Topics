_____ ?

db _ ?.c..('mydb.db')
db.r_f.. _ ?.Row
cursor _ db.cursor()
cursor.e..('''SELECT name, email, phone FROM users''')
___ row __ cursor:
    # row['name'] returns the name column in the query, row['email'] returns email column.
    print('{0} : {1}, {2}'.f..(row['name'], row['email'], row['phone']))
db.close()

