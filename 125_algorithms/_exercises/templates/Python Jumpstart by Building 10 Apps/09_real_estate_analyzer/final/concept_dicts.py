lookup  {}
lookup  d..()
lookup  {'age': 42, 'loc': 'Italy'}
lookup  d..(age42, loc'Italy')


class Wizard:
    ___ __init__(self, name, level):
        self.level  level
        self.name  name


gandolf  Wizard("Gladolf", 42)
print(gandolf.__dict__)

print(lookup)
print(lookup['loc'])

lookup['cat']  'Fun code demos'

__ 'cat' __ lookup:
    print(lookup['cat'])

# Suppose these came from a data source, e.g. database, web service, etc
# And we want to randomly access them
_______ collections

User  collections.namedtuple('User', 'id, name, email')
users  [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm'),
]

lookup  d..()
___ u __ users:
    lookup[u.email]  u

print(lookup['user4@talkpython.fm'])


# LAMBDAS
___ find_significant_numbers(nums, predicate):
    ___ n __ nums:
        __ predicate(n):
            yield n


numbers  [1, 1, 2, 3, 5, 8, 13, 21, 34]
sig  find_significant_numbers(numbers, l.... x: x % 2 __ 1)
print(l..(sig))
