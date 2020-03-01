# ___ src.interface_segregation_principle.stage_1_header_interface ______ user_repository
#
#
# c_ MySQLUsersRepository u__.U..
#     ___ save user __ N..
#         print("Saves a user in MySQL but doesn't commit it to DB")
#
#     ___ commit user __ N..
#         print("commit a user in MySQL")
#
#     ___ saveAll user __ N..
#         print("Saves a list of users in MySQL")
