# bob = ('Bob', 40.5, 'dev', 'mgr'  # Tuple record
# print ?
# # ('Bob', 40.5, ['dev', 'mgr'])
# print ? 0 ? 2  # Access by position
# # ('Bob', ['dev', 'mgr'])
#
# bob = di.. name_'Bob', age_40.5, jobs_'dev', 'mgr'  # Dictionary record
# print ?
# # {'jobs': ['dev', 'mgr'], 'name': 'Bob', 'age': 40.5}
# print ?  name , ? jobs  # Access by key
# # ('Bob', ['dev', 'mgr'])
#
# print ___ ?.va..  # Values to tuple
# # (['dev', 'mgr'], 'Bob', 40.5)
# print(l.. ?.it.. # Items to tuple list
# # [('jobs', ['dev', 'mgr']), ('name', 'Bob'), ('age', 40.5)]
#
# f____ co___ ______ n_t_  # Import extension type
# Rec = n_t_ 'Rec', |'name', 'age', 'jobs'  # Make a generated class
# bob = ? Bob , age_40.5, jobs_|dev mgr  # A named-tuple record
# print ?
# # Rec(name='Bob', age=40.5, jobs=['dev', 'mgr'])
# print ? 0 ? 2  # Access by position
# # ('Bob', ['dev', 'mgr'])
# print ?.n.. ?.j..  # Access by attribute
# # ('Bob', ['dev', 'mgr'])
#
# O = ?._asd..  # Dictionary-like form
# print ?  name , ?  jobs  # Access by key too
# # ('Bob', ['dev', 'mgr'])
# print ?
# # OrderedDict([('name', 'Bob'), ('age', 40.5), ('jobs', ['dev', 'mgr'])])
#
# bob = R.. Bob 40.5 | dev , mgr  # For both tuples and named tuples
# n.. a.. j.. _ ?  # Tuple assignment (Chapter 11)
# print n.. j..
# # ('Bob', ['dev', 'mgr'])
# ___ x __ ?
#     print ?  # Iteration context (Chapters 14, 20)
# # ...prints Bob, 40.5, ['dev', 'mgr']...
#
# bob =  name Bob age 40.5 jobs dev mgr
# j.. n.. a.. _ ?.va..
# print n.. j..  # Dict equivalent (but order may vary)
# # ('Bob', ['dev', 'mgr'])
#
# ___ x i_ ?
#     print ? ?  # Step though keys, index values
# # ...prints values...
# ___ x __ ?.va..
#
#     print(x)  # Step through values view
# # ...prints values...
