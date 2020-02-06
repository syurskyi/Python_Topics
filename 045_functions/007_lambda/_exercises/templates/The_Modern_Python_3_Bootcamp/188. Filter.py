# users = [
#     {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
#     {"username": "katie", "tweets": ["I love my cat"]},
#     {"username": "jeff", "tweets": []},
#     {"username": "bob123", "tweets": []},
#     {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
#     {"username": "guitar_gal", "tweets": []}
# ]
#
# # extract inactive users using filter:
# inactive_users _ l.. f.. l.. u; no. ? 'tweets'| u..
#
# # extract inactive users using list comprehension:
# inactive_users2 + user __ ? __ u.. __ no. ? "tweets"|
#
# # extract usernames of inactive users w/ map and filter:
# usernames = l.. m.. l... user ? "username"|.u.. ,
#                      f.. l.. u; no. ? 'tweets'| ?
#
# # extract usernames of inactive users w/ list comprehension
# usernames2 = user "username"|.u.. ___ ? __ u.. __ no. ? "tweets"|
