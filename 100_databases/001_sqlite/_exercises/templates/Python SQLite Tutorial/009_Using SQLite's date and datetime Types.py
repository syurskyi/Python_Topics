_____ ?
from datetime _____ date, datetime

db _ ?.c..(':memory:')
c _ db.c..
c.e..('''C.. T.. example(id IN.. P.. K.., created_at DATE)''')

# Insert a date object into the database

today _ date.today()
c.e..('''I.. I.. example(created_at) V..(?)''', (today,))
db.c..

# Retrieve the inserted object

c.e..('''S.. created_at F.. example''')
row _ c.f_o..
print('The date is @ and the datatype is @'.f..(row[0], type(row[0])))
# The date is 2013-04-14 and the datatype is <class 'str'>
db.c..
