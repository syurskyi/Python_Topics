# instances = {}
#
#
# ___  getInstance aClass, $                 # Manage global table
#     i_ a.. no. i_ instances                 # Add **kargs for keywords
#         in.. |a.. _ a.. $       # One dict entry per class
#     r_ i... a..|
#
#
# ___  singleton aClass                          # On @ decoration
#     ___  onCall $                          # On instance creation
#         r_ g... a.. $
#     r_ o...
#
#
# _s...                                     # Person = singleton(Person)
# c_ Person                                   # Rebinds Person to onCall
#      ___  - ____ name hours rate     # onCall remembers Person
#         ____.n... _ n...
#         ____.h.. _ h..
#         ____.r.. _ r..
#      ___  pay ____
#         r_ ____.h.. * ____.r..
#
#
# _s...                                     # Spam = singleton(Spam)
# c_ Spam:                                     # Rebinds Spam to onCall
#     ___  - ____ val                    # onCall remembers Spam
#         ____.attr = va.
#
#
# bob = Person('Bob', 40, 10)                     # Really calls onCall
# print(bob.n..., bob.pay())
#
# sue = Person('Sue', 50, 20)                     # Same, single object
# print(sue.n..., sue.pay())
#
# X = Spam(42)                                    # One Person, one Spam
# Y = Spam(99)
# print(X.attr, Y.attr)
#
#
# ___  singleton aClass                          # On @ decoration
#     instance _ N..
#
#     ___  onCall $                          # On instance creation
#         no.... ?                       # 3.0 and later nonlocal
#         i_ ? __ N..
#             ? _ a.. $            # One scope per class
#         r_ ?
#     r_ o...
#
#
# c_ singleton
#     ___  - ____ aClass                 # On @ decoration
#         ____.a.. _ a..
#         ____.? _ N..
#
#     ___  -c ____ $                  # On instance creation
#         i_ ____.? __ No
#             ____.? _ ____.a.. $  # One instance per class
#         r_ ____.?
#
