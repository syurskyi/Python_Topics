# # A User class with both a class attribute
# c_ User
#
#     active_users = 0
#
#     ___ - ____ first last age
#         ____.?  ?
#         ____.?  ?
#         ____.?  ?
#         U__.? +_ 1
#
#     ___ logout ____
#         U_.? -_ 1
#         r_ _*____.f..| has logged out"
#
#     ___ full_name ____
#         r_ _*____.f..| ____.l.."
#
#     ___ initials ____
#         r_ _*____.f.. 0 |.____.l.. 0 |."
#
#     ___ likes ____, thing
#         r_ _*____.f..| likes thing|"
#
#     ___ is_senior ____
#         r_ ____.a.. >_ 65
#
#     ___ birthday ____
#         ____.age +_ 1
#         r_ _*Happy ____.age| th, ____.f..|"
#
#
# # print(user1.likes("Ice Cream"))
# # print(user2.likes("Chips"))
#
# # print(user2.initials())
# # print(user1.initials())
#
# # print(user2.is_senior())
# # print(user1.age)
# # print(user1.birthday())
# # print(user1.age)
# # user1.say_hi()
#
#
# print(User.active_users)
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.active_users)
# print(user2.logout())
# print(User.active_users)
