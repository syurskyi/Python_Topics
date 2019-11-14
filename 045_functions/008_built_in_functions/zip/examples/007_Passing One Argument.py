a = [1, 2, 3]
zipped = zip(a)
list(zipped)
# [(1,), (2,), (3,)]

integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)  # Three input iterables
list(zipped)
# [(1, 'a', 4.0), (2, 'b', 5.0), (3, 'c', 6.0)]