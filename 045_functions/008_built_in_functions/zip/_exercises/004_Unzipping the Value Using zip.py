coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c, v =  zip(*resultList)
print('c =', c)
print('v =', v)

# [('x', 3), ('y', 4), ('z', 5)]
# c = ('x', 'y', 'z')
# v = (3, 4, 5)