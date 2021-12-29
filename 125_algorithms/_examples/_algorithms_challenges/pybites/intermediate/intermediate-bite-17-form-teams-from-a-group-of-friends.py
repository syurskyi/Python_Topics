from itertools import combinations
from itertools import permutations


"""
Write a function called friends_teams that takes a list of friends,
a team_size (type int, default=2) and order_does_matter (type bool, default False).

Return all possible teams. Hint: if order matters (order_does_matter=True),
the number of teams would be greater.

See the tests for more details. Enjoy :)
"""

def my_solution_friends_teams(friends: list, team_size: int, order_does_matter: bool = False) -> list:

    if order_does_matter:
        result = permutations(friends, team_size)
    else:
        result = combinations(friends, team_size)
    return list(result)

result = my_solution_friends_teams(['Bob', 'Alice', 'John', 'Mary', 'Theo', 'Julius'], 2, order_does_matter = True)
print(result)

