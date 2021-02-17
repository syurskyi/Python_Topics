users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# extract inactive users using filter:
inactive_users = l..(f..(l_____ u: not u['tweets'], users))

# extract inactive users using list comprehension:
inactive_users2 = [user ___ user __ users __ not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = l..(m__(l_____ user: user["username"].upper(),
                     f..(l_____ u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() ___ user __ users __ not user["tweets"]]

print(inactive_users)
print(inactive_users2)
print(usernames)
print(usernames2)