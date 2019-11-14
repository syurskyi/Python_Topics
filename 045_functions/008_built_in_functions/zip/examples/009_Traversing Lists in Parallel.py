letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')

# Letter: a
# Number: 0
# Letter: b
# Number: 1
# Letter: c
# Number: 2

# Here, you iterate through the series of tuples returned by zip() and unpack the elements into l and n.
# When you combine zip(), for loops, and tuple unpacking, you can get a useful and Pythonic idiom for traversing two
# or more iterables at once.
#
# You can also iterate through more than two iterables in a single for loop. Consider the following example,
# which has three input iterables:

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')


# Letter: a
# # Number: 0
# # Operator: *
# # Letter: b
# # Number: 1
# # Operator: /
# # Letter: c
# # Number: 2
# # Operator: +