import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)


# Example 2
squares = map(lambda x: x ** 2, a)
print(list(squares))


# Example 3
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)


# Example 4
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)


# Example 5
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)
