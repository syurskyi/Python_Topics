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
        # TODO 1: you code
        r.. f"{first_name.t..} {last_name.t..}"

    $
    ___ username
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        # TODO 2: you code

        r.. f"{first_name[0].l..}{last_name[:7].l..}"

    # TODO 3: you code
    #
    # add a __str__ and a __repr__
    # see: https://stackoverflow.com/a/1438297
    # "__repr__ is for devs, __str__ is for customers"
    #
    # see also TESTS for required output

    ___ __str__
        r.. f"{get_full_name} ({username})"

    ___  -r
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        r.. f'{__class__.__name__}("{first_name}", "{last_name}")'
