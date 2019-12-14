bob = ('Bob', 40.5, ['dev', 'mgr']) # Tuple record
print(bob)
# ('Bob', 40.5, ['dev', 'mgr'])
print(bob[0], bob[2])  # Access by position
# ('Bob', ['dev', 'mgr'])

bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])  # Dictionary record
print(bob)
# {'jobs': ['dev', 'mgr'], 'name': 'Bob', 'age': 40.5}
print(bob['name'], bob['jobs'])  # Access by key
# ('Bob', ['dev', 'mgr'])

print(tuple(bob.values()))  # Values to tuple
# (['dev', 'mgr'], 'Bob', 40.5)
print(list(bob.items())) # Items to tuple list
# [('jobs', ['dev', 'mgr']), ('name', 'Bob'), ('age', 40.5)]

from collections import namedtuple  # Import extension type
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])  # Make a generated class
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])  # A named-tuple record
print(bob)
# Rec(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob[0], bob[2])  # Access by position
# ('Bob', ['dev', 'mgr'])
print(bob.name, bob.jobs)  # Access by attribute
# ('Bob', ['dev', 'mgr'])

O = bob._asdict()  # Dictionary-like form
print(O['name'], O['jobs'])  # Access by key too
# ('Bob', ['dev', 'mgr'])
print(O)
# OrderedDict([('name', 'Bob'), ('age', 40.5), ('jobs', ['dev', 'mgr'])])

bob = Rec('Bob', 40.5, ['dev', 'mgr'])  # For both tuples and named tuples
name, age, jobs = bob  # Tuple assignment (Chapter 11)
print(name, jobs)
# ('Bob', ['dev', 'mgr'])
for x in bob:
    print(x)  # Iteration context (Chapters 14, 20)
# ...prints Bob, 40.5, ['dev', 'mgr']...

bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
job, name, age = bob.values()
print(name, job)  # Dict equivalent (but order may vary)
# ('Bob', ['dev', 'mgr'])

for x in bob:
    print(bob[x])  # Step though keys, index values
# ...prints values...
for x in bob.values():

    print(x)  # Step through values view
# ...prints values...
