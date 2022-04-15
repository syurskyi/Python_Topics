'''
In this Bite you are presented with another class, User this time.

Like last Bite you are asked to complete it, see the TODOs in the code below:

Complete the get_full_name property (more on properties here) that prints first and last name separated by a space.
Complete the username property following its docstring.
Complete the special representation dunder methods: __str__ and __repr__. Look at the tests what they should return.
Brace yourself for some bonus learning for a twist we added in __repr__ (but as it's a Beginner Bite we give you a hint!)
Apart from Ned's awesome answer on SO, to give you an idea about the difference between __str__ and __repr__, check out
how datetime implements them:

>>> from datetime import datetime
>>> dt = datetime.now()
>>> str(dt)
'2019-02-04 23:05:27.376407'
>>> repr(dt)
'datetime.datetime(2019, 2, 4, 23, 5, 27, 376407)'
Good luck and keep calm and code in Python!
'''

c_ User:
    """A User class
       (Django's User model inspired us)
    """

    ___ - , first_name, last_name
        """Constructor, base values"""
        first_name first_name
        last_name last_name

    $
    ___ get_full_name
        """Return first separated by a whitespace
           and using title case for both.
        """
        # TODO 1: you code
        r.. f"{first_name.capitalize()} {last_name.capitalize()}"

    $
    ___ username
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        f first_name[0:1].l..
        l last_name[0:7].l..
        r.. f"{f}{l}"

    # TODO 3: you code
    #
    # add a __str__ and a __repr__
    # see: https://stackoverflow.com/a/1438297
    # "__repr__ is for devs, __str__ is for customers"
    #
    # see also TESTS for required output

    ___ -s
        r.. f"{first_name.capitalize()} {last_name.capitalize()} ({username})"

    ___  -r
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        r.. _* -c .-n (\"{first_name}\", \"{last_name}\")"

u ? "bob", "belderbos")

print(u.get_full_name)
print(u.username)
print(u. -r