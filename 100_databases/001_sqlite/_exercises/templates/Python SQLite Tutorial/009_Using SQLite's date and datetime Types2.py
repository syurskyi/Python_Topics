
# The problem is that if you inserted a date object in the database,
# most of the time you are expecting a date object when you retrieve it, not a string object.
# This problem can be solved passing PARSE_DECLTYPES and PARSE_COLNAMES to the connect method:

_____ ?
from datetime _____ date, datetime

db _ ?.c..(':memory:', detect_types_?.PARSE_DECLTYPES|?.PARSE_COLNAMES)
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
# The date is 2013-04-14 and the datatype is <class 'datetime.date'>

# Changing the connect method, the database now is returning a date object.
# The sqlite3 module uses the column's type to return the correct type of object.
# So, if we need to work with a datetime object, we must declare the column in the table as a timestamp type:

db.c..
