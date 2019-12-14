print('{name} {job} {name}'.format(name='Bob', job='dev'))
print('%(name)s %(job)s %(name)s' % dict(name='Bob', job='dev'))
D = dict(name='Bob', job='dev')
print('{0[name]} {0[job]} {0[name]}'.format(D))  # Method, key references
print('{name} {job} {name}'.format(**D))  # Method, dict-to-args
print('%(name)s %(job)s %(name)s' % D)  # Expression, key references
