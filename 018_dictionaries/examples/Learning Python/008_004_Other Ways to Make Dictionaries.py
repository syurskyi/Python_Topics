__author__ = 'sergejyurskyj'


# NOTE: in the following, you must use "dbm" instead of "anydbm"
# in Python 3.X (this module was renamed in 3.X only).  Also note
# that these are incomplete, partial examples as is.
"""
import anydbm
file = anydbm.open("filename")     # Link to file
file['key'] = 'data'               # Store data by key
data = file['key']                 # Fetch data by key

import cgi
form = cgi.FieldStorage()          # Parse form data
if 'name' in form:
    showReply('Hello, ' + form['name'].value)
"""


{'name': 'mel', 'age': 45}            # Traditional literal expression

D = {}                                # Assign by keys dynamically
D['name'] = 'mel'
D['age'] = 45

print('#' * 52 + ' dict keyword argument form')
print(dict(name='mel', age=45))              # dict keyword argument form

print('#' * 52 + ' dict key/value tuples form')
print(dict([('name', 'mel'), ('age', 45)]))  # dict key/value tuples form

print('#' * 52)
print(dict.fromkeys(['a', 'b'], 0))
