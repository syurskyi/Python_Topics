# List Comprehensions A First Detailed Look

L = [1, 2, 3, 4, 5]

for i in range(len(L)):          # how to use range to change a list as we step across it
    L[i] += 10

print(L)

L = [x + 10 for x in L]          #list comprehension expression
print(L)


# List Comprehension Basics

L = [1, 2, 3, 4, 5]

L = [x + 10 for x in L]   #  list comprehension simply looks like a backward for loop.
print(L)


res = []
for x in L:
    res.append(x + 10)

print(res)

# Using List Comprehensions on Files

f = open('script1.py')
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]
print(lines)


lines = [line.rstrip() for line in open('script1.py')]
print(lines)

print([line.upper() for line in open('script1.py')])

print([line.rstrip().upper() for line in open('script1.py')])

print([line.split() for line in open('script2.py')])

print([line.replace(' ', '!') for line in open('script2.py')])

print([('sys' in line, line[0]) for line in open('script1.py')])

# Extended List Comprehension Syntax

lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']
print(lines)

res = []
for line in open('script2.py'):
    if line[0] == 'p':
        res.append(line.rstrip())
print(res)


print([x + y for x in 'abc' for y in 'lmn'])

res = []
for x in 'abc':
    for y in 'lmn':
        res.append(x + y)
print(res)

# Why You Will Care List Comprehensions and map
print(open('myfile').readlines())

print([line.rstrip() for line in open('myfile').readlines()])

print([line.rstrip() for line in open('myfile')])

print(list(map((lambda line: line.rstrip()), open('myfile'))))

listoftuple = [('bob', 35, 'mgr'), ('mel', 40, 'dev')]

print([age for (name, age, job) in listoftuple])

print(list(map((lambda row: row[1]), listoftuple)))


# Comprehension Syntax Summary
# List comprehension: builds list

print([x * x for x in range(10)])

# Comprehension Syntax Summary
# Generator expression: produces items
# Parens are often optional

print((x * x for x in range(10)))

# Comprehension Syntax Summary
# Set comprehension, new in 3.0, {x, y} is a set in 3.0 too

print({x * x for x in range(10)} )



# And re-working this into a list comprehension:
#
n = 10
iter_cycl = CyclicIterator('NSWE')
[f'{i}{next(iter_cycl)}' for i in range(1, n+1)]
#
# Of course, there's an easy alternative way to do this as well, using: repetition, zip
# a list comprehension

n = 10
list(zip(range(1, n+1), 'NSWE' * (n//4 + 1)))

# There's actually an even easier way yet, and that's to use our CyclicIterator, but instead of building it ourselves, we can simply use the one provided by Python in the standard library!!

import itertools
n = 10
iter_cycl = CyclicIterator('NSWE')
[f'{i}{next(iter_cycl)}' for i in range(1, n+1)]

n = 10
iter_cycl = i


