# List Comprehensions Versus map

res = []
for x in 'spam':
    res.append(ord(x))  # Manual results collection

print(res)

res = list(map(ord, 'spam'))  # Apply function to sequence
print(res)

res = [ord(x) for x in 'spam']  # Apply expression to sequence
print(res)

print([x ** 2 for x in range(10)])

print(list(map((lambda x: x ** 2), range(10))))

# Adding Tests and Nested Loops - filter
# range(5)

print([x for x in range(5) if x % 2 == 0])

print(list(filter((lambda x: x % 2 == 0), range(5))))

res = []
for x in range(5):
    if
x % 2 == 0:
res.append(x)
print(res)

# Adding Tests and Nested Loops - filter
# range(10)

print([x ** 2 for x in range(10) if x % 2 == 0])

print(list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))))

# Adding Tests and Nested Loops - filter
#  for x in

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

res = []
for x in [0, 1, 2]:
    for
y in [100, 200, 300]:
res.append(x + y)
print(res)

print([x + y for x in 'spam' for y in 'SPAM'])

# Adding Tests and Nested Loops - filter
# for x in range(5)

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])

res = []
for x in range(5):
    if
x % 2 == 0:
for y in range(5):
    if
y % 2 == 1:
res.append((x, y))
print(res)
