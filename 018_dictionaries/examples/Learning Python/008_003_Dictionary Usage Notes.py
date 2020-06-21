__author__ = 'sergejyurskyj'

"""
L = []
L[99] = 'spam'
Traceback (most recent call last):
File "<stdin>", line 1, in ?
IndexError: list assignment index out of range
"""
D = {}
D[99] = 'spam'
print(D[99])
print(D)


Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
print(Matrix)

print('#' * 52 + ' separates statements')
X = 2; Y = 3; Z = 4               # ; separates statements
Matrix[(X, Y, Z)]
print(Matrix)

"""
Matrix[(2,3,6)]
Traceback (most recent call last):
File "<stdin>", line 1, in ?
KeyError: (2, 3, 6)
"""

print('#' * 52 + ' Check for key before fetch')

if (2, 3, 6) in Matrix:           # Check for key before fetch
    print(Matrix[(2, 3, 6)])      # See Chapter 12 for if/else
else:
    print(0)


print('#' * 52 + ' Try to index')

try:
    print(Matrix[(2, 3, 6)])      # Try to index
except KeyError:                  # Catch and recover
    print(0)                      # See Chapter 33 for try/except


############################################ DON'T UNDERSTAND
print('#' * 52 + ' Exists; fetch and return')
Matrix.get((2, 3, 4), 0)          # Exists; fetch and return
print(Matrix)

Matrix.get((2,3,6), 0)            # Doesn't exist; use default arg
print(Matrix)


print('#' * 52)
rec = {}
rec['name'] = 'mel'
rec['age'] = 45
rec['job'] = 'trainer/writer'
print(rec['name'])

print('#' * 52)

mel = {'name': 'Mark',
       'jobs': ['trainer', 'writer'],
       'web': 'www.rmi.net/�lutz',
       'home': {'state': 'CO', 'zip':80513}}

print(mel['name'])
print(mel['jobs'])
print(mel['jobs'][1])
print(mel['home']['zip'])


print('#' * 52)
rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer/manager'
print(rec['name'])

print('#' * 52)
rec = {'name': 'Bob',
       'jobs': ['developer', 'manager'],
       'web': 'www.bobs.org/˜Bob',
       'home': {'state': 'Overworked', 'zip': 12345}}

print(rec['name'])
print(rec['jobs'])
print(rec['jobs'][1])
print(rec['home']['zip'])

############################################ DON'T UNDERSTAND why don't work
"""
print('#' * 52)
db = []
db.append(rec)                  # A list "database"
db.append(other)
print(db)

db[0]['jobs']

db = {}
db['bob'] = rec                 # A dictionary "database"
db['sue'] = other
db['bob']['jobs']
print(db)
"""