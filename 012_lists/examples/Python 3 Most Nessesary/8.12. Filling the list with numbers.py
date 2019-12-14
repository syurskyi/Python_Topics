print(list(range(11)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(list(range(1, 16)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


print(list(range(15, 0, -1)))
# [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


import random
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(arr, 3))
# [1, 9, 5]
print(random.sample(range(300), 5))
# [259, 294, 142, 292, 245]
