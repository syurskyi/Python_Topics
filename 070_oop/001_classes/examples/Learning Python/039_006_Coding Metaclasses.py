class Meta(type):
    def __new__(meta, classname, supers, classdict):
        # Run by inherited type.__call__
        return type.__new__(meta, classname, supers, classdict)


class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)


class Eggs:
    pass


print('making class')


class Spam(Eggs, metaclass=MetaOne):  # Inherits from Eggs, instance of Meta
    data = 1  # Class data attribute

    def meth(self, arg):  # Class method attribute
        pass


print('making instance')
X = Spam()
print('data:', X.data)

