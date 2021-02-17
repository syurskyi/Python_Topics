users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# To sort users by their username
so__(users, k.._l_____ user: user['username'])

# Finding our most active users...
# Sort users by number of tweets, descending
so__(users, k.._l_____ user: le.(user["tweets"]), reverse=True)

# ANOTHER EXAMPLE DATA SET==================================
songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
so__(songs, k.._l_____ s: s['playcount'])
