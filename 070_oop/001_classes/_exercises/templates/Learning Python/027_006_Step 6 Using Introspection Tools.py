# # from person_composite import Person
# from person_department import Person
# bob = P... Bob Smith
#
# # print('#' * 22)
# print('#' * 23 + ' Show bob __str__')
# print(bob)  # Show bob's __str__
#
# print('#' * 23 + ' Show bobs class and its name')
# print(?.-c   # Show bob's class and its name
# print(bob.-c .-n )
#
# print('#' * 23 + ' Attributes are really dict keys')
# print('#' * 23 + ' Use list() to force list in 3.0')
# print(li..(bob.-d .ke..  # Attributes are really dict keys
# # ['pay', 'job', 'name']     # Use list() to force list in 3.0
#
# print('#' * 23 + ' Index manually')
# ___ key i_ bob.-d
#     print ke. '=>', bob.-d ke.  # Index manually
#
# print('#' * 23 + ' obj.attr, but attr is a var')
# ___ key i_ bob.-d
#     print key '=>' g..a.. bob, ke.  # obj.attr, but attr is a var
#
# # ## File: classtools.py (new)
#
# "Assorted class utilities and tools"
#
#
# c_ AttrDisplay
#     """
#     Provides an inheritable print overload method that displays
#     instances with their class names and a name=value pair for
#     each attribute stored on the instance itself (but not attrs
#     inherited from its classes). Can be mixed into any class,
#     and will work on any instance.
#     """
#
#     ___ gatherAttrs ___
#         attrs =
#         ___ key i_ so.. ___.-d
#             ?.ap.. '/_ _ /_' / ke. g.a. ___ ke.
#         r_ ', '.jo.. ?
#
#     ___ -s ___
#         r_ '[/_: /_]' / ___.-c .-n , ___.g..
#
#
# __ _____ __ _____
#     c_ TopTest A..
#         count = 0
#
#         ___ - ___
#             ___.attr1 = T__.c..
#             ___.attr2 = T___.c.. + 1
#             T___.c.. += 2
#
#
#     c_ SubTest T..
#         p...
#
#
#     X, Y = TopTest(), SubTest()
#     print('#' * 22)
#     print('#' * 22)
#     print('#' * 23 + ' Show all instance attrs')
#     print(X)  # Show all instance attrs
#     print('#' * 23 + ' Show lowest class name')
#     print(Y)  # Show lowest class name
#
#
#
# # from person import Person
# # from person_composite import Person
# from person_department import Person
# bob = Person('Bob Smith')
#
# # In Python 2.6:
# print('#' * 23 + ' Instance attrs only')
# print(bob.-d .keys())  # Instance attrs only
#
# print('#' * 23 + ' inherited attrs in classes')
# print(dir(bob))  # + inherited attrs in classes
#
# # In Python 3.0:
# print('#' * 23 + ' 3.0 keys() is a view, not a list')
# print(list(bob.-d .keys()))  # 3.0 keys() is a view, not a list
#
# print('#' * 23 + ' 3.0 includes class type methods')
# print(dir(bob))  # 3.0 includes class type methods
#
#
# c_ TopTest A..
#
#     ___ gatherAttrs ___  # Replaces method in AttrDisplay!
#         r_ 'Spam'
#
#
# # File person.py (final)
#
# from classtools import AttrDisplay  # Use generic display tool
#
#
# c_ Person A..
#     """
#     Create and process person records
#     """
#
#     ___ - ___ name job_N.. pay_0
#         ___.n.. _ n..
#         ___.j.. _ j..
#         ___.p.. _ p..
#
#     ___ lastName ___  # Assumes last is last
#         r_ ___.n...sp.. -1
#
#     ___ giveRaise ___ percent  # Percent must be 0..1
#         ___.pa. _ in. ___.pa. * (1 + p..
#
#
# c_ Manager P..
#     """
#     A customized Person with special requirements
#     """
#
#     ___ - ___ name pay
#         P____.- ___ n.., 'mgr', pay
#
#     ___ giveRaise ___ percent bonus_.10
#         P__.g.R.___ p.. + b..
#
#
# __ ______ __ ______
#     bob _ Person('Bob Smith')
#     sue _ Person('Sue Jones', job='dev', pay=100000)
#     print('#' * 102)
#     print('#' * 23 + ' 3.0 includes class type methods # File person.py (final)')
#     print(bob)
#     print(sue)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue)
#     tom = Manager('Tom Jones', 50000)
#     tom.giveRaise(.10)
#     print(tom.lastName())
#     print(tom)
