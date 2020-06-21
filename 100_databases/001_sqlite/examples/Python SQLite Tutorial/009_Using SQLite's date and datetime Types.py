import sqlite3
from datetime import date, datetime

db = sqlite3.connect(':memory:')
c = db.cursor()
c.execute('''CREATE TABLE example(id INTEGER PRIMARY KEY, created_at DATE)''')

# Insert a date object into the database

today = date.today()
c.execute('''INSERT INTO example(created_at) VALUES(?)''', (today,))
db.commit()

# Retrieve the inserted object

c.execute('''SELECT created_at FROM example''')
row = c.fetchone()
print('The date is {0} and the datatype is {1}'.format(row[0], type(row[0])))
# The date is 2013-04-14 and the datatype is <class 'str'>
db.close()
