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
        r.. s..(self.first_name).t.. + ' ' + s..(self.last_name).t..

    @property
    ___ username(self):
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        r.. s..(self.first_name)[:1].lower() + s..(self.last_name)[:7].lower()

    ___ __str__(self):
        r.. s..(self.get_full_name) + ' (' + s..(self.username) + ')'

    ___ __repr__(self):
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        r.. f'User("{self.first_name}", "{self.last_name}")'