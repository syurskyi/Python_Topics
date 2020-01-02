# L = ['Bob', 40.5, ['dev', 'mgr']]    # List-based "record"
# print ? 0
# 'Bob'
# print ? 1                          # Positions/numbers for fields
# # 40.5
# print ? 2 1
# # 'mgr'
#
# D = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
# print ? n..
# # 'Bob'
# print ? a..                       # Dictionary-based "record"
# # 40.5
# print ? jobs 1                   # Names mean more than numbers
# 'mgr'
#
# D = di.. name_'Bob' age_40.5 jobs_'dev', 'mgr'
# print ? n..
# # 'Bob'
# ? j__.re.. mgr
# print ?
# # {'jobs': ['dev'], 'age': 40.5, 'name': 'Bob'}
#
# D _    # dict
# ? state1 _ T..                     # A visited-state dictionary
# print state1 __ ?
# # True
# S _   # set
# ?.a.. ?                        # Same, but with sets
# print state1 __ ?
# # True