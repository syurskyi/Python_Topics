# # A User class with both instance attributes and instance methods
# c_ User
#     active_users _ 0
#
#     ??
#     ____ display_active_users ___
#         r_ _*There are currently |___.?| active users
#
#     ??
#     ____ from_string ___ data_str
#         first, last, age = ?.sp.. ","
#         r_ ___ ?, ? in. ?
#
#     ____ - ____, first, last, age
#         ____.?  ?
#         ____.?  ?
#         ____.?  ?
#         ?.? +_ 1
#
#     ____ logout ____
#         ?.? -_ 1
#         r_ _* ____.f..| has logged out
#
#     ____ full_name ____
#         r_ _* ____.f..| ____.l..|
#
#     ____ initials ____
#         r_ _* ____.f.. 0 |. ____.l.. 0 |.
#
#     ____ likes ____, thing
#         r_ _* ____.f..| likes |thing
#
#     ____ is_senior ____
#         r_ ____.a.. >_ 65
#
#     ____ birthday ____
#         ____.a.. += 1
#         r_ _*Happy |____.a..|th, |____.f..
#
# # user1 = User("Joe", "Smith", 68)
# # user2 = User("Blanca", "Lopez", 41)
# # print(User.display_active_users())
# # user1 = User("Joe", "Smith", 68)
# # user2 = User("Blanca", "Lopez", 41)
# # print(User.display_active_users())
#
#
# tom = User.from_string("Tom,Jones,89")
# print(?.f..)
# print(?.full_name())
# print(?.birthday())
