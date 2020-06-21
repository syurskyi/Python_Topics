
# The problem is that if you inserted a date object in the database,
# most of the time you are expecting a date object when you retrieve it, not a string object.
# This problem can be solved passing PARSE_DECLTYPES and PARSE_COLNAMES to the connect method:

import sqlite3
from datetime import date, datetime

db = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
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
# The date is 2013-04-14 and the datatype is <class 'datetime.date'>

# Changing the connect method, the database now is returning a date object.
# The sqlite3 module uses the column's type to return the correct type of object.
# So, if we need to work with a datetime object, we must declare the column in the table as a timestamp type:

db.close()
