from itertools import combinations, permutations


___ friends_teams(friends, team_size=2, order_does_matter=False):

    __ order_does_matter:
        teams = [team for team in permutations(friends, team_size)]
    else:
        teams = [team for team in combinations(friends, team_size)]
    return teams


# if __name__ == "__main__":
#    friends_teams(friends, 2, True)