from itertools ______ combinations, permutations

___ friends_teams(friend_list: list, team_size: int, order_does_matter: bool = False) -> list:
    __ order_does_matter:
        r_ [x for x in permutations(friend_list,team_size)]
    ____
        r_ [x for x in combinations(friend_list,team_size)]
