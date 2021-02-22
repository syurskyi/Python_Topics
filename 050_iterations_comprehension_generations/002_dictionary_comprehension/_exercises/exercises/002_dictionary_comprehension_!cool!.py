# # Comprehension Syntax Summary
# # Dictionary comprehension
# # x
# print ? ? * ? ___ ? __ r... 10   # # Dictionary comprehension
#
# # Comprehending Set and Dictionary Comprehensions
# # Comprehension
# # Generator and type name
# #  Set comprehension equivalent
# # Dict comprehension equivalent
# # x
print({x * x for x in range(10)})    # dict)}
print(set(x * x for x in range(10)))    # not dict
print({x: x * x for x in range(10)})  # dict
print(dict(x, x * x) for x in range(10))

res = set()    # set
for x in range(10):
    res.add(x * x)
print(res)

res = {}    # dictionary
for x in range(10):
    res[x] = x * x

print(res)
#
# # Notice that although both forms accept iterators, they have no notion of generating
# # results on demand both forms build objects all at once. If you mean to produce keys
# # and values upon request, a generator expression is more appropriate:

G = ((x, x * x) for x in range(10))  # generator expression
print(next(G))
#
print(next(G))
#
# # Extended Comprehension Syntax for Sets and Dictionaries
# # Lists are ordered
# # But sets are not
# # Neither are dict keys
# # Lists keep duplicates
# #  But sets do not
# # Neither do dict keys
#
print()
print()
print([x * x for x in range(10) if x % 2 == 0])  # list
print({x * x for x in range(10) if x % 2 == 0})  # set
print({x: x * x for x in range(10) if x % 2 == 0})  # dict
# # x, y
# print ? + ? ___ ? __ 1, 2, 3 ___ ? __ 4, 5, 6 # list
# print ? + ? ___ ? __ 1, 2, 3 ___ ? __ 4, 5, 6 # set
# print ? ? ___ ? __ 1, 2, 3 ___ ? __ 4, 5, 6   # dict
