class Person:
    def __init__(self, name):               # On [Person()]
        self._name = name                   # Triggers __setattr__!

    def __getattr__(self, attr):            # On [obj.undefined]
        if attr == 'name':                  # Intercept name: not stored
            print('fetch...')
            return self._name               # Does not loop: real attr
        else:                               # Others are errors
            raise AttributeError(attr)

    def __setattr__(self, attr, value):     # On [obj.any = value]
        if attr == 'name':
            print('change...')
            attr = '_name'                  # Set internal name
        self.__dict__[attr] = value         # Avoid looping here

    def __delattr__(self, attr):            # On [del obj.any]
        if attr == 'name':
            print('remove...')
            attr = '_name'                  # Avoid looping here too
        del self.__dict__[attr]             # but much less common

bob = Person('Bob Smith')           # bob has a managed attribute
print(bob.name)                     # Runs __getattr__
bob.name = 'Robert Smith'           # Runs __setattr__
print(bob.name)
del bob.name                        # Runs __delattr__

print('-'*20)
sue = Person('Sue Jones')           # sue inherits property too
print(sue.name)
#print(Person.name.__doc__)         # No equivalent here
print('#' * 52 + '  ')
print('#' * 52 + '  ')



    # # Replace __getattr__ with this
    #
    # def __getattribute__(self, attr):                 # On [obj.any]
    #     if attr == 'name':                            # Intercept all names
    #         print('fetch...')
    #         attr = '_name'                            # Map to internal name
    #     return object.__getattribute__(self, attr)    # Avoid looping here


# #######################################################################################

class Person:
    def __init__(self, name):               # On [Person()]
        self._name = name                   # Triggers __setattr__!

    def __getattribute__(self, attr):                 # On [obj.any]
        if attr == 'name':                            # Intercept all names
            print('fetch...')
            attr = '_name'                            # Map to internal name
        return object.__getattribute__(self, attr)    # Avoid looping here

    def __setattr__(self, attr, value):     # On [obj.any = value]
        if attr == 'name':
            print('change...')
            attr = '_name'                  # Set internal name
        self.__dict__[attr] = value         # Avoid looping here

    def __delattr__(self, attr):            # On [del obj.any]
        if attr == 'name':
            print('remove...')
            attr = '_name'                  # Avoid looping here too
        del self.__dict__[attr]             # but much less common

bob = Person('Bob Smith')           # bob has a managed attribute
print(bob.name)                     # Runs __getattr__
bob.name = 'Robert Smith'           # Runs __setattr__
print(bob.name)
del bob.name                        # Runs __delattr__

print('-'*20)
sue = Person('Sue Jones')           # sue inherits property too
print(sue.name)
#print(Person.name.__doc__)         # No equivalent here
