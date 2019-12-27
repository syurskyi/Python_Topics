# # NOTE: this is person.py, despite the getattr.py filename in
# # its first command line (a minor typo in the first printing)
#
#
# ### file: person.py
#
# c_ Person:
#     ___ - ____, name, job_N. pay_0
#         ____.n.. _ n..
#         ____.j.. _ j..
#         ____.p.. _ p..
#
#     ___ lastName ____
#         r_ ____.n...sp.. -1
#
#     ___ giveRaise ____ percent
#         ____.p.. _ in. ____.p.. *  1 + p...
#
#     ___ -s ____
#         r_ '[Person: /_, /_]' / ____.n.. ____.p..
#
#
# c_ Manager
#     ___ - ___ name pay
#         ____.person _ P___ n.. 'mgr' p..  # Embed a Person object
#
#     ___ giveRaise ____ percent bonus_.10
#         ____.p____.g.. p.. + b  # Intercept and delegate
#
#     ___ -g ____ attr
#         r_ g.... ____.p.... a...  # Delegate all other attrs
#
#     ___ -s ____
#         r_ st. ____.pe..  # Must overload again (in 3.0)
#
#
# __ ______ __ ______
#     sue _ P___ 'Sue Jones', job_'dev', pay_100000
#     print( ?.l..
#     ?.g.. .10
#     print(sue)
#     tom _ M___ Tom Jones', 50000  # Manager.__init__
#     print(t__.l..  # Manager.__getattr__ -> Person.lastName
#     ?.g___ .10  # Manager.giveRaise -> Person.giveRaise
#     print(tom)  # Manager.__str__ -> Person.__str__
#
#
# # Delete the Manager __str__ method
#
# c_ Manager
#     ___ - ____ name pay
#         ____.person _ P___ n.., 'mgr', p..  # Embed a Person object
#
#     ___ giveRaise ____ percent bonus_.10
#         ____.p____.g.. p... + b...  # Intercept and delegate
#
#     ___ -g ____ attr
#         r_ g... ____.p.. a..  # Delegate all other attrs
#
#
# # Replace __getattr_ with __getattribute__
#
# c_ Manager                                           # Use (object) in 2.6
#     ___ - ____ name, pay
#         ____.p... _ P__ n.., 'mgr', p..           # Embed a Person object
#
#     ___ giveRaise ____ percent bonus_.10
#         ____.p__.g... p... + b..           # Intercept and delegate
#
#     ___ -g ____ attr
#         print('**', a...
#         i_ a.. i_ 'person', 'giveRaise'
#             r_ obj_. -g ____ a..  # Fetch my attrs
#         e___
#             r_ g... ____.p.. a..           # Delegate all others
#
#
# # Code __getattribute__ differently to minimize extra calls
#
# c_ Manager
#     ___ - ____ name pay)
#         ____.p... _ P.. n.., 'mgr', p..
#
#     ___ -g ____ attr
#         print '**' a
#         person _ obj__. -g ____ 'person'
#         i_ attr __ 'giveRaise':
#             r_ l_____ percent p___.g... p... + .10
#         e___
#             r_ g... p..  a...
#
#     ___ -s ____
#         person _ obj___. -g ____ 'person
#         r_ st. p..
