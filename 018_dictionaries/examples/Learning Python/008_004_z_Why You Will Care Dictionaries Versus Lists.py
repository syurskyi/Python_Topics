L = ['Bob', 40.5, ['dev', 'mgr']]    # List-based "record"
print(L[0])
'Bob'
print(L[1])                          # Positions/numbers for fields
# 40.5
print(L[2][1])
# 'mgr'

D = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
print(D['name'])
# 'Bob'
print(D['age'])                       # Dictionary-based "record"
# 40.5
print(D['jobs'][1])                   # Names mean more than numbers
'mgr'

D = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(D['name'])
# 'Bob'
D['jobs'].remove('mgr')
print(D)
# {'jobs': ['dev'], 'age': 40.5, 'name': 'Bob'}

D = {}
D['state1'] = True                     # A visited-state dictionary
print('state1' in D)
# True
S = set()
S.add('state1')                        # Same, but with sets
print('state1' in S)
# True