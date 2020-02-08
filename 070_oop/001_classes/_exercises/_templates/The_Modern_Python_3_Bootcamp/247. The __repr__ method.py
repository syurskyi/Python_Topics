# # A User class with both instance attributes and instance methods
# c_ User
#     active_users _ 0
#
#     ??
#     ___ display_active_users ___
#         r_ _*There are currently |___.?| active users"
#
#     ??
#     ___ from_string ___ data_str
#         first, last, age _ ?.sp.. ","
#         r_ ___ ? ? in. ?
#
#     ___ -  ____ first last age
#         ____.?  ?
#         ____.?  ?
#         ____.?  ?
#         ?.? +_ 1
#     # NEW CODE
#
#     ___ -r
#         r_ _* ____.first| is ____.a..
#     # NEW CODE
#
#     ___ logout ____
#             ?.? -_ 1
#             r_ _*|____.f..| has logged out"
#
#         ___ full_name____
#             r_ _*|____.f..| ____.l..|
#
#         ___ initials ____
#             r_ _*|____.f.. 0 |. ____.l.. 0 |."
#
#         ___ likes ____ thing
#             r_ _*|____.f..| likes |?
#
#         ___ is_senior ____
#             r_ ____.a.. >_ 65
#
#         ___ birthday ____
#             ____.a.. += 1
#             r_ _*Happy |____.a..|th, ____.f.|
#
#
# tom = User.from_string("Tom,Jones,89")
#
# j = User("judy", "steele", 18)
# j = str(j)
# print(j)
