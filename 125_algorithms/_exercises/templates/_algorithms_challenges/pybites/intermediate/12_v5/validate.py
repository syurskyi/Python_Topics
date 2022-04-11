# ____ c.. _______ n..
#
# User  n..('User', 'name role expired')
# USER, ADMIN  'user', 'admin'
# SECRET  'I am a very secret token'
#
# julian  ? n.._'Julian', r.._USER, e.._F..
# bob  ? n.._'Bob' r.._USER e.._T..
# pybites  ? n.._'PyBites'  r.._ADMIN, e.._F..
# USERS  ? ? ?
#
#
# # define exception classes here
# c_ UserDoesNotExist E..
#     p..
#
#
# c_ UserAccessExpired E..
#     p..
#
#
# c_ UserNoPermission E..
#     p..
#
#
# ___ get_secret_token username
#     ___ user __ ?
#         __ ?.n.. __ ?
#             __ ?.e..:
#                 r.. ? _*No access available for ?
#             __ ?.r.. __ A..
#                 r.. S..
#             r.. ? _*User ? has insufficient permission
#     r.. ? _*User ? does not exist
