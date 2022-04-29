# c_ User
#     """A User class
#        (Django's User model inspired us)
#     """
#
#     ___ -  first_name, last_name
#         """Constructor, base values"""
#         ? ?
#         ? ?
#
#     $
#     ___ get_full_name
#         """Return first separated by a whitespace
#            and using title case for both.
#         """
#         r.. s.. ? .t.. + ' ' + s.. ? .t..
#
#     $
#     ___ username
#         """A username consists of the first char of
#            the user's first_name and the first 7 chars
#            of the user's last_name, both lowercased.
#
#            If this is your first property, check out:
#            https://pybit.es/property-decorator.html
#         """
#         r.. s.. ? |1 .l.. + s.. ? |7 .l..
#
#     ___ -s
#         r.. s.. ? + ' (' + s.. ? + ')'
#
#     ___  -r
#         """Don't hardcode the class name, hint: use a
#            special attribute of self.__class__ ...
#         """
#         r.. _* -c.-n "?" "?")'