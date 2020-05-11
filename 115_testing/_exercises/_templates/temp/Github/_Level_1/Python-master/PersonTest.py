#
# ______ u__
#
# # This is the class we want to test. So, we need to ______ it
# ______ P.. __ PC..
#
#
# c_ Test ?.?
#     """
#     The basic class that inherits unittest.TestCase
#     """
#     person _ ?.P..  # instantiate the Person Class
#     user_id _ # list  # variable that stores obtained user_id
#     user_name _ # list  # variable that stores person name
#
#     # test case function to check the Person.set_name function
#     ___ test_0_set_name
#         print("Start set_name test\n")
#         """
#         Any method which starts with ``test_`` will considered as a test case.
#         """
#         ___ i __ ra.. 4
#             # initialize a name
#             name _ 'name' + st. ?
#             # store the name into the list variable
#             u_n_.a.. ?
#             # get the user id obtained from the function
#             u_i. _ p__.s.. ?
#             # check if the obtained user id is null or not
#             aINN.. ?  # null user id will fail the test
#             # store the user id to the list
#             ?.a.. ?
#         print("user_id length = ", le. ?
#         print ?
#         print("user_name length = ", le. ?
#         print ?
#         print("\nFinish set_name test\n")
#
#     # test case function to check the Person.get_name function
#     ___ test_1_get_name
#         print("\nStart get_name test\n")
#         """
#         Any method that starts with ``test_`` will be considered as a test case.
#         """
#         length _ le. u_i.  # total number of stored user information
#         print("user_id length = " ?
#         print("user_name length = ", le. ?
#         ___ i __ ra.. 6
#             # if i not exceed total length then verify the returned name
#             __ ? < ?
#                 # if the two name not matches it will fail the test case
#                 aE.. u_n.. ? p__.g_n.. u_i ?
#             ____:
#                 print("Testing for get_name no user test")
#                 # if length exceeds then check the 'no such user' type message
#                 aE.. 'There is no such user', p__.g_n.. ?
#         print("\nFinish get_name test\n")
#
#
# __ _____ __ _____
#     # begin the unittest.main()
#     ?.?