from access import Private, Public
# look on file access

@Private('age')                             # Person = Private('age')(Person)
class Person:                               # Person = onInstance with state
    def __init__(self, name, age):
        self.name = name
        self.age = age                     # Inside accesses run normally


X = Person('Bob', 40)
print(X.name)                                     # Outside accesses validated
# 'Bob'
X.name = 'Sue'
print(X.name)
# 'Sue'
# X.age            # TypeError: private attribute fetch: age

# X.age = 'Tom'   # TypeError: private attribute change: age


@Public('name')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


X = Person('bob', 40)                       # X is an onInstance
X.name                                      # onInstance embeds Person
# 'bob'
X.name = 'Sue'
X.name
# 'Sue'
# X.age           # TypeError: private attribute fetch: age
# X.age = 'Tom'   # TypeError: private attribute change: age