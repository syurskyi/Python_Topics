from itertools import combinations, permutations

def friends_teams(friend_list, team_size=2, order_does_matter=False):
    #print(len(friend_list), team_size, order_does_matter)
    return list(combinations(friend_list, team_size)) if not order_does_matter else list(permutations(friend_list, team_size))

friends = 'Bob Dante Julian Martin'.split()

print(friends)

print(friends_teams(friends, 2, True))

