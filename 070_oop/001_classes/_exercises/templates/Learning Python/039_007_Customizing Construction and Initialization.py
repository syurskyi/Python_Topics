class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaOne init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


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
