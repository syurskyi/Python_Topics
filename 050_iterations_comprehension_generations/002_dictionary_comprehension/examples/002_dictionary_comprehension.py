# Comprehension Syntax Summary
# Dictionary comprehension

print({x: x * x for x in range(10)})

# Comprehending Set and Dictionary Comprehensions
# Comprehension
# Generator and type name
#  Set comprehension equivalent
# Dict comprehension equivalent

print({x * x for x in range(10)})
set(x * x for x in range(10))
print({x: x * x for x in range(10)})
print(dict((x, x * x) for x in range(10)))

res = set()
for x in range(10):
    res.add(x * x)
print(res)

res = {}
for x in range(10):
    res[x] = x * x

print(res)

# Notice that although both forms accept iterators, they have no notion of generating
# results on demand—both forms build objects all at once. If you mean to produce keys
# and values upon request, a generator expression is more appropriate:

G = ((x, x * x) for x in range(10))
print(next(G))

print(next(G))

# Extended Comprehension Syntax for Sets and Dictionaries
# Lists are ordered
# But sets are not
# Neither are dict keys
# Lists keep duplicates
#  But sets do not
# Neither do dict keys

print([x * x for x in range(10) if x % 2 == 0])
print({x * x for x in range(10) if x % 2 == 0})
print({x: x * x for x in range(10) if x % 2 == 0})
print([x + y for x in [1, 2, 3] for y in [4, 5, 6]])
print({x + y for x in [1, 2, 3] for y in [4, 5, 6]})
print({x: y for x in [1, 2, 3] for y in [4, 5, 6]})
