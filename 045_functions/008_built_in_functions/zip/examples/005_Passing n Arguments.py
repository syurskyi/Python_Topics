numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
zipped  # Holds an iterator object
# <zip object at 0x7fa4831153c8>
type(zipped)
# <class 'zip'>
list(zipped)
# [(1, 'a'), (2, 'b'), (3, 'c')]

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
list(zip(s1, s2))
# [(1, 'a'), (2, 'c'), (3, 'b')]