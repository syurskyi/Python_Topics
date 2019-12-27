# from access import Private, Public
# # look on file access
# 
# _P.. 'age'                             # Person = Private('age')(Person)
# c_ Person                               # Person = onInstance with state
#     ___ - ____ name age
#         ____.n.. _ n..
#         ____.a.. _ a..                     # Inside accesses run normally
# 
# 
# X = ? 'Bob', 40
# print(X.name)                                     # Outside accesses validated
# # 'Bob'
# X.name = 'Sue'
# print(X.name)
# # 'Sue'
# # X.age            # TypeError: private attribute fetch: age
# 
# # X.age = 'Tom'   # TypeError: private attribute change: age
# 
# 
# _P.. 'name'
# c_ Person
#     ___ - ____ name age
#         ____.n.. _ n..
#         ____.a.. _ a..
# 
# 
# X _ ?('bob', 40)                       # X is an onInstance
# ?.n..                                     # onInstance embeds Person
# # 'bob'
# ?.n.. _ 'Sue'
# ?.n..
# # 'Sue'
# # X.age           # TypeError: private attribute fetch: age
# # X.age = 'Tom'   # TypeError: private attribute change: age
