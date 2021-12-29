import itertools


___ friends_teams(friends, team_size=2, order_does_matter=False):
    __ order_does_matter:
        func = itertools.permutations
    else:
        func = itertools.combinations
    return func(friends, team_size)