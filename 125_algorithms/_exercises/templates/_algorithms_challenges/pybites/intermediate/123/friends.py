____ c.. _______ defaultdict

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.s..
ids = r..(l..(names))
users = d..(z..(ids, names))  # 0: bob, 1: julian, etc


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


___ get_friend_with_most_friends(friendships, users=users
   """Receives the friendships list of user ID pairs,
      parse it to see who has most friends, return a tuple
      of (name_friend_with_most_friends, his_or_her_friends)"""
   friend_frequency = defaultdict(l..)

   ___ f1, f2 __ friendships:
      friend_frequency[f1].a..(f2)
      friend_frequency[f2].a..(f1)

   most_friends = 0
   previous_value = 0
   ___ key, value __ friend_frequency.i..:
      __ l..(value) >= previous_value:
         most_friends = key
         previous_value = l..(value)
      
   r.. (users[most_friends], s..([users[friend] ___ friend __ friend_frequency[most_friends]]))


# if __name__ == "__main__":
#    print(get_friend_with_most_friends(friendships))