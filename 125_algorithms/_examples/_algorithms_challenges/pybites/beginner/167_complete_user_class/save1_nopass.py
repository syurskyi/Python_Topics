class User:
    """A User class
       (Django's User model inspired us)
    """

    def __init__(self, first_name, last_name):
        """Constructor, base values"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_full_name(self):
        """Return first separated by a whitespace
           and using title case for both.
        """
        return str(self.first_name).title() + ' ' + str(self.last_name).title()

    @property
    def username(self):
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        return str(self.first_name)[:1].lower() + str(self.last_name)[:7].lower()

    def __str__(self):
        return str(self.get_full_name) + ' (' + str(self.username) + ')'

    def __repr__(self):
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        return f'User("{self.first_name}", "{self.last_name}")'