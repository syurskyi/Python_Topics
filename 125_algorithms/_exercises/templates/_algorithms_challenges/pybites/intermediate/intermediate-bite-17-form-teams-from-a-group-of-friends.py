____ i.. _______ combinations
____ i.. _______ permutations


"""
Write a function called friends_teams that takes a list of friends,
a team_size (type int, default=2) and order_does_matter (type bool, default False).

Return all possible teams. Hint: if order matters (order_does_matter=True),
the number of teams would be greater.

See the tests for more details. Enjoy :)
"""

___ my_solution_friends_teams(friends: l.., team_size: i.., order_does_matter: b.. = F..) __ l..:

    __ order_does_matter:
        result = permutations(friends, team_size)
    ____
        result = c..friends, team_size)
    r.. l..(result)

result = my_solution_friends_teams( 'Bob', 'Alice', 'John', 'Mary', 'Theo', 'Julius' , 2, order_does_matter = T..)
print(result)

