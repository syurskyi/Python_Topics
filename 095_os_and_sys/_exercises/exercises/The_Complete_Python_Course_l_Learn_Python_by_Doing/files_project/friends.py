# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to `nearby_friends.txt`

friends _ input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

people _ o..('people.txt', 'r')
people_nearby _ [line.strip() ___ line __ people.readlines()]

people.close()

friends_set _ set(friends)
people_nearby_set _ set(people_nearby)

friends_nearby_set _ friends_set.intersection(people_nearby_set)

nearby_friends_file _ o..('nearby_friends.txt', 'w')

___ friend __ friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.w..(f'{friend}\n')

nearby_friends_file.close()
