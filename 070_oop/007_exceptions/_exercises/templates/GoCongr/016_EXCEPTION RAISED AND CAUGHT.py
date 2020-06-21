# # EXCEPTION RAISED AND CAUGHT
# ___
#     x = 'spam'[99]
# _____ I...
#     print('except run')
# f____
#     print('finally run')
# print('after run')
#
# # NO EXCEPTION RAISED
# ___
#     x = 'spam'[3]
# _____ I...
#     print('except run')
# f____
#     print('finally run')
# print('after run')
#
# # NO EXCEPTION RAISED, WITH ELSE
# ___
#     x = 'spam'[3]
# _____ I...
#     print('except run')
# ____
#     print('else run')
# f____
#     print('finally run')
# print('after run')