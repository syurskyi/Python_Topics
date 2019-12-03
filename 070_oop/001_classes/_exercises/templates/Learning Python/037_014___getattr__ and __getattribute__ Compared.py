class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):            # On undefined attrs only
        print('get: ' + attr)               # Not attr1: inherited from class
        return 3                            # Not attr2: stored on instance

X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)

print('-'*40)


class GetAttribute(object):                 # (object) needed in 2.6 only
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):       # On all attr fetches
        print('get: ' + attr)               # Use superclass to avoid looping here
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)

