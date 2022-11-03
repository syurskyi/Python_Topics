# # List Comprehensions Versus map

res = []  # list
for x in 'spam':
    res.append(ord(x))  # Manual results collection

print(res)

res = list(map(ord, 'spam'))  # Apply function to sequence
print(res)

res = [ord(x) for x in 'spam']  # Apply expression to sequence
print(res)

print([x ** 2 for x in range(10)])

print(list(map((lambda x: x ** 2), range(10))))

# # Adding Tests and Nested Loops - filter
# # range(5)

print([x for x in range(5) if x % 2 == 0])

print(list(filter((lambda x: x % 2 == 0), (range(5)))))

res = []    # list
for x in range(5):
    if x % 2 == 0:
        res.append(x)
    print(res)

# # Adding Tests and Nested Loops - filter
# # range(10)

print([x ** 2 for x in range(10) if x % 2 == 0])

print(list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))))

# # Adding Tests and Nested Loops - filter
# #  for x in
#
# res _ x + y ___ x __ |0 1 2| ___ y __ |100 200 300
# print r..
#
# res _     # list
# ___ x __ 0 1 2
#     ___
# y i_ 100 200 300
# res.ap.. x + y
# print r..
#
# print x + y ___ ? __ 'spam' ___ ? __ 'SPAM'
#
# # Adding Tests and Nested Loops - filter
# # for x in range(5)
#
# print |||x y ___ x __ ra.. 5 __ x % 2 __ 0 ___ y __ ra.. 5 __ y % 2 __ 1
#
# res _  # list
# ___ x __ ra.. 5
#     __ ? % 2 __ 0
#         ___ y __ ra.. 5
#             __ ? % 2 __ 1
#                 ?.ap.. x y
#     print ?
