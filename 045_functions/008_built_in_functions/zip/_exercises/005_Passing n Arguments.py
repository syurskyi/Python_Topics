numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped)  # Holds an iterator object
# # <zip object at 0x7fa4831153c8>
print(type(zipped))
# # <class 'zip'>
print(list(zipped))
# # [(1, 'a'), (2, 'b'), (3, 'c')]

s1 = {2, 3, 1}
s2 =  {'b', 'a', 'c'}
print(list(zip(s1, s2)))
# # [(1, 'a'), (2, 'c'), (3, 'b')]