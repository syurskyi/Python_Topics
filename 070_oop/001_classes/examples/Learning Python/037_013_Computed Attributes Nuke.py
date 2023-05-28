class AttrSquare:
    def __init__(self, start):
        self.value = start  # Triggers __setattr__!

    def __getattr__(self, attr):  # On undefined attr fetch
        if attr == 'X':
            return self.value ** 2  # value is not undefined
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):  # On all attr assignments
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value


A = AttrSquare(3)  # 2 instances of class with overloading
B = AttrSquare(32)  # Each has different state information

print(A.X)  # 3 ** 2
A.X = 4
print(A.X)  # 4 ** 2
print(B.X)  # 32 ** 2


class AttrSquare:
    def __init__(self, start):
        self.value = start  # Triggers __setattr__!

    def __getattribute__(self, attr):  # On all attr fetches
        if attr == 'X':
            return self.value ** 2  # Triggers __getattribute__ again!
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):  # On all attr assignments
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)

    def __getattribute__(self, attr):
        if attr == 'X':
            return object.__getattribute__(self, 'value') ** 2


