__author__ = 'sergejyurskyj'

print(3 in [1, 2, 3])                    # Membership

# for x in [1, 2, 3]:
#     print(x, end=' ')                    # Iteration
# print()

res = [c * 4 for c in 'SPAM']            # List comprehensions
print(res)



res = []
for c in 'SPAM':                          # List comprehension equivalent
    res.append(c * 4)
print(res)

print(list(map(abs, [-1, -2, 0, 1, 2])))  # map function across sequence
