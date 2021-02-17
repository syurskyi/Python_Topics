numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()
print(result)

# Converting itertor to list
resultList = list(result)
print(resultList)
#
# Two iterables are passed
result = zip(numberList, strList)
print(list(result))
#
# # Converting itertor to set
# resultSet = set(result)
# print(resultSet)
#
# # []
# # {(2, 'two'), (3, 'three'), (1, 'one')}

