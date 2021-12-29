class User:
    """A User class
       (Django's User model inspired us)
    """

    ___ __init__(self, first_name, last_name):
        """Constructor, base values"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    ___ get_full_name(self):
        """Return first separated by a whitespace
           and using title case for both.
        """
        # TODO 1: you code
        return '{} {}'.format(self.first_name.title(),self.last_name.title())

    @property
    ___ username(self):
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        # TODO 2: you code
        return '{}{}'.format(self.first_name.lower()[0], self.last_name.lower()[:7])

    # TODO 3: you code
    #
    # add a __str__ and a __repr__
    # see: https://stackoverflow.com/a/1438297
    # "__repr__ is for devs, __str__ is for customers"
    #
    # see also TESTS for required output

    ___ __str__(self):
        return '{} ({})'.format(self.get_full_name, self.username)
        

    ___ __repr__(self):
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        #return "'{}({} {})'".format(self.__class__.__name__, self.first_name, self.last_name)
        return f"{self.__class__.__name__}(\"{self.first_name}\", \"{self.last_name}\")"

bob = User('bob', 'belderbos')
print(bob.get_full_name)
print(bob.username)
print(str(bob))
print(repr(bob))