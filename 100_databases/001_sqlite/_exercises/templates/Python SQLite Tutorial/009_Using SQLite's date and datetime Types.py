_____ ?
from datetime _____ date, datetime

db _ ?.c..(':memory:')
c _ db.c..
c.e..('''C.. T.. example(id IN.. P.. K.., created_at DATE)''')

# Insert a date object into the database

today _ date.today()
c.e..('''INSERT INTO example(created_at) VALUES(?)''', (today,))
db.c..

# Retrieve the inserted object

c.e..('''SELECT created_at FROM example''')
row _ c.fetchone()
print('The date is {0} and the datatype is {1}'.f..(row[0], type(row[0])))
# The date is 2013-04-14 and the datatype is <class 'str'>
db.c..
