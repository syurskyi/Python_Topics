c_ User:
    """A User class
       (Django's User model inspired us)
    """

    ___ - , first_name, last_name):
        """Constructor, base values"""
        first_name = first_name
        last_name = last_name

    $
    ___ get_full_name
        """Return first separated by a whitespace
           and using title case for both.
        """
        r.. s..(first_name).t.. + ' ' + s..(last_name).t..

    $
    ___ username
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        r.. s..(first_name)[:1].l.. + s..(last_name)[:7].l..

    ___ __str__
        r.. s..(get_full_name) + ' (' + s..(username) + ')'

    ___  -r
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        r.. f'{__class__.__name__}("{first_name}", "{last_name}")'