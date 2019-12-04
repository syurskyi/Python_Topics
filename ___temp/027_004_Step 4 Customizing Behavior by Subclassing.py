# c_ Person
#     ___ -  ____ n.. job_None pay_0
#         ____.n.. _ n..
#         ____.j.. _ j..
#         ____.p.. _ p..
#
#     ___ lastName ____
#         r_ ____.n...sp.. -1
#
#     ___ giveRaise ____ percent
#         ____.p.. _ in. ____.p.. * 1 + p..
#
#     ___ -s ____                                         # Added method
#         r_  Person: /_, /_ / ____.n.. ____.p..     # String to print
#
#
# c_ Manager Person
#     ___ giveRaise ____ percent bonus_.10
#         ____.p.. _ in.  ____.p.. * (1 + p.. + b...  # Bad: cut-and-paste
#
#
# c_ Manager..
#     ___ giveRaise ____ percent bonus_.10
#         P__.giveRaise ____ p.. + b..  # Good: augment original
#
#
# # Add customization of one behavior in a subclass
#
# c_ Person
#     ___ -  ____ name job_None pay_0
#         ____.n.. _ n..
#         ____.j.. _ j..
#         ____.p.. _ p..
#
#     ___ lastName ____
#         r_ ____.n...sp.. -1
#
#     ___ giveRaise ____ percent
#         ____.p.. _ in. ____.p.. * (1 + p..
#
#     ___ -s ____
#         r_ Person: /_ /_ / ____.n.. ____.p..
#
#
# c_ Manager P..
#     ___ giveRaise ____ percent bonus_.10  # Redefine at this level
#         P__.g.R _____  p.. + b..  # Call Person's version
#
#
# __ _______ __ ____
#     bob _ P___ Bob Smith
#     sue _ P____ 'Sue Jones', job_'dev', pay_100000
#     print(bob)
#     print(sue)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue)
#     print('#' * 52 + ' Make a Manager: - ')
#     tom _ Manager('Tom Jones', 'mgr', 50000)  # Make a Manager: -
#     tom.giveRaise(.10)  # Runs custom version
#     print('#' * 52 + ' Runs inherited method')
#     print(tom.lastName())  # Runs inherited method
#     print('#' * 52 + ' Runs inherited __str__')
#     print(tom)  # Runs inherited __str__
#
# print('#' * 22)
# print('#' * 22)
# print('#' * 22)
# print('#' * 23 + ' Process objects generically')
# print('#' * 23 + ' Run this objects giveRaise')
# print('#' * 23 + ' Run the common __str__')
# __ ______ __ ______
#     print('--All three--')
#     ___ object i_ b.. s.. t..  # Process objects generically
#         ?.g.R.(.10)  # Run this objects giveRaise
#         print ?  # Run the common __str__
#
# '''
# c_ Person:
#     ___ lastName(____):
#         pass
#
#     ___ giveRaise(____):
#         pass
#
#     ___ __str__(____): pass
#
#
# c_ Manager(Person):  # Inherit
#     ___ giveRaise(____, ...): pass  # Customize
#
#     ___ someThingElse(____, ...): pass  # Extend
# '''
# """
# tom = Manager()
# tom.lastName()  # Inherited verbatim
# tom.giveRaise()  # Customized version
# tom.someThingElse()  # Extension here
# print(tom)  # Inherited overload method
# """
