numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)

result = zip(numbersList, strList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)


# {(2, 'TWO'), (3, 'THREE'), (1, 'ONE')}
# {(2, 'two', 'TWO'), (1, 'one', 'ONE')}