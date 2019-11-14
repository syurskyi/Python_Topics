letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data1 = list(zip(letters, numbers))
data1
# [('b', 2), ('a', 4), ('d', 3), ('c', 1)]
data1.sort()  # Sort by letters
data1
# [('a', 4), ('b', 2), ('c', 1), ('d', 3)]
data2 = list(zip(numbers, letters))
data2
# [(2, 'b'), (4, 'a'), (3, 'd'), (1, 'c')]
data2.sort()  # Sort by numbers
data2
# [(1, 'c'), (2, 'b'), (3, 'd'), (4, 'a')]

letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data = sorted(zip(letters, numbers))  # Sort by letters
data
# [('a', 4), ('b', 2), ('c', 1), ('d', 3)]