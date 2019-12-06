# # EXCEPTION RAISED AND CAUGHT
# t__
#     x = 'spam'[99]
# e____ I...
#     print('e____ run')
# f____
#     print('finally run')
# print('after run')
#
# # NO EXCEPTION RAISED
# t__
#     x = 'spam'[3]
# e____ I...
#     print('e____ run')
# f____:
#     print('finally run')
# print('after run')
#
# # NO EXCEPTION RAISED, WITH ELSE
# t__
#     x = 'spam'[3]
# e____ I...
#     print('e____ run')
# e___
#     print('else run')
# f____
#     print('finally run')
# print('after run')