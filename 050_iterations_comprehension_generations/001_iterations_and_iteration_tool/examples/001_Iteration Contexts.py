# Iteration Contexts
# Use file iterators

for line in open('script2.py'):
    print(line.upper(), end='')

# Iteration Contexts
# Use List Comprehension

uppers = [line.upper() for line in open('script2.py')]
print(uppers)

# Iteration Contexts
# Use Map

print(map(str.upper, open('script1.py')))

# Iteration Contexts
# Use List and Map

print(list(map(str.upper, open('script2.py'))))

# Iteration Contexts
# Use Sorted

print(sorted(open('script2.py')))

# Iteration Contexts
# Use Zip

print(list(zip(open('script2.py'), open('script2.py'))))

# Iteration Contexts
# Use Enumerate

print(list(enumerate(open('script2.py'))))

# Iteration Contexts
# Use Filter

print(list(filter(bool, open('script2.py'))))

# Iteration Contexts
# Use Reduce

print(functools.reduce(operator.add, open('script2.py')))

# Iteration Contexts
# Use Sum

print(sum([3, 2, 4, 1, 5, 0]))

# Iteration Contexts
# Use Any

print(any(['spam', '', 'ni']))

# Iteration Contexts
# Use All

print(all(['spam', '', 'ni']))

# Iteration Contexts
# Use Max

print(max([3, 2, 5, 1, 4]))

# Iteration Contexts
# Use Min

print(min([3, 2, 5, 1, 4]))

# Iteration Contexts
# Use Max for file

print(max(open('script2.py')))

# Iteration Contexts
# Use Min for file

print(min(open('script2.py')))

# Iteration Contexts
# Use List for file
print(list(open('script2.py')))

# Iteration Contexts
# Use Tuple for file
print(tuple(open('script2.py')))

# Iteration Contexts
# Slice assignment
L = [11, 22, 33, 44]
L[1:3] = open('script2.py')
print(L)

# Iteration Contexts
# list.extend method
L = [11]
L.extend(open('script2.py'))
print(L)
