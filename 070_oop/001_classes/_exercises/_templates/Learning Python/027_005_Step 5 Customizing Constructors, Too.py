# # Add customization of constructor in a subclass
#
#
# c_ Person:
#     ___ -  ____ name job_N.. pay_0
#         ____.n... _ n...
#         ____.j.. _ j..
#         ____.p.. _ p..
#
#     ___ lastName ____
#         r_ ____.n....sp.. -1
#
#     ___ giveRaise ____ percent
#         ____.p.. _ in. ____.p.. * (1 + p...
#
#     ___ -s ____
#         r_ Person: /_, /_  / ____.n..., ____.p..
#
#
# c_ Manager P..
#     ___ -  ____ name pay  # Redefine constructor
#         Person.-  ____ n... 'mgr' p..  # Run original with 'mgr'
#
#     ___ giveRaise ____ percent bonus_.10
#         P___.g.. ____ p.. + b..
#
#
# __ _____ __ _____
#     bob _ P___ Bob Smith
#     sue _ P____ 'Sue Jones', job_'dev', pay_100000
#     print('#' * 22)
#     print('#' * 23 + ' Add customization of constructor in a subclass')
#     print(bob)
#     print(sue)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue)
#     tom _ Manager('Tom Jones', 50000)  # Job name not needed:
#     tom.giveRaise(.10)  # Implied/set by c_
#     print(tom.lastName())
#     print(tom)
#
#
# # Embedding-based Manager alternative
#
# c_ Person:
#     ___ -  ____ name job_None pay_0
#         ____.n... _ n...
#         ____.j.. _ j..
#         ____.p.. _ p..
#
#     ___ lastName ____
#         r_ ____.n....sp.. -1
#
#     ___ giveRaise ____ percent
#         ____.p.. _ in. ____.p.. * (1 + p..
#
#     ___ -s  ____
#         r_ Person: /_, /_ / ____.n... ____.p..
#
#
# c_ Manager
#     ___ -  ____ name pay
#         ____.person _ Person(n... 'mgr' p..  # Embed a Person object
#
#     ___ giveRaise ____ percent, bonus_.10
#         ____.p__.g.. p.. + b..  # Intercept and delegate
#
#     ___ __g ____ attr
#         r_ g... ____.p.. a..  # Delegate all other attrs
#
#     ___ -s  ____
#         r_ st. ____.p..  # Must overload again (in 3.0)
#
# __ _______ __ ______
#     bob _ P.. 'Bob Smith
#     sue _ P..('Sue Jones', job_'dev', pay_100000)
#     print('#' * 22)
#     print('#' * 23 + ' Embedding-based Manager alternative')
#     print(bob)
#     print(sue)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue)
#     tom _ Manager('Tom Jones', pay_100000)  # Job name not needed:
#     tom.giveRaise(.10)  # Implied/set by class
#     print(tom.lastName())
#     print(tom)
# # Aggregate embedded objects into a composite
#
#
# bob _ Person('Bob Smith')
# sue _ Person('Sue Jones', job_'dev', pay_100000)
# tom _ Manager('Tom Jones', 50000)
#
# c_ Department
#     ___ -  ____ 0a.
#         ____.members _ li.. a..
#
#     ___ addMember ____ person
#         ____.m__.ap.. ?
#
#     ___ giveRaises ____ percent
#         ___ person i_ ____.m..
#             ?.g.R. p..
#
#     ___ showAll ____
#         ___ person i_ ____.m..
#             print ?
#
#
# development _ Department(bob, sue)  # Embed objects in a composite
# development.addMember(tom)
# development.giveRaises(.10)  # Runs embedded objects' giveRaise
# development.showAll()  # Runs embedded objects' __str__s
#
