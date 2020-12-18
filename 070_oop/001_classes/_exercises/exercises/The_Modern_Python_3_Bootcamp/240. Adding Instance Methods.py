# # A User class with both instance attributes and instance methods
# c_ User
#     ___ - ____ first last age
#         ____.?  ?
#         ____.?  ?
#         ____.?  ?
#
#     ___ full_name ____
#         r_ _* ____.f.. ____.l..
#
#     ___ initials ____
#         r_ _* ____.f.. 0 . ____.l.. 0 .
#
#     ___ likes ____ thing
#         r_ _* ____.f.. likes t..
#
#     ___ is_senior ____
#         r_ ____.a.. >_ 65
#
#     ___ birthday ____
#         ____.a.. +_ 1
#         r_ _*Happy ____.a.. th, ____.f..
#
#
# user1 = ?("Joe", "Smith", 68)
# user2 = ?("Blanca", "Lopez", 41)
#
# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))
#
# print(user2.initials())
# print(user1.initials())
#
# print(user2.is_senior())
# print(user1.age)  # Print age before we update it
# print(user1.birthday())  # updates age
# print(user1.age)  # Print new value of age
