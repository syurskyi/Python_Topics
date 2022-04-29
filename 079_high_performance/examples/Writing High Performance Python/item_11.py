import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print(letters)


# Example 2
longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)


# Example 3
longest_name = None
max_letters = 0
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)


# Example 4
longest_name = None
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)


# Example 5
names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)
