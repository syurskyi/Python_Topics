import itertools
___ friends_teams(friends,team_size=2,order_does_matter=False):


    __ order_does_matter:
        return itertools.permutations(friends,team_size)
    else:
        return itertools.combinations(friends,team_size)







