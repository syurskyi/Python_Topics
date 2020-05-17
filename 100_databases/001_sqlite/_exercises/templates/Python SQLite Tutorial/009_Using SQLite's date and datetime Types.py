_____ ?
from datetime _____ date, datetime

db _ ?.c..(':memory:')
c _ db.cursor()
c.e..('''CREATE TABLE example(id INTEGER PRIMARY KEY, created_at DATE)''')

# Insert a date object into the database

today _ date.today()
c.e..('''INSERT INTO example(created_at) VALUES(?)''', (today,))
db.commit()

# Retrieve the inserted object

c.e..('''SELECT created_at FROM example''')
row _ c.fetchone()
print('The date is {0} and the datatype is {1}'.f..(row[0], type(row[0])))
# The date is 2013-04-14 and the datatype is <class 'str'>
db.close()
