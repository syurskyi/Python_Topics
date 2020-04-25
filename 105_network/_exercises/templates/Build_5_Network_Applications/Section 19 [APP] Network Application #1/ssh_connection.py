# ______ pa..
# ______ __.pa__
# ______ t__
# ______ ___
# ______ __
#
# #Checking username/password file
# #Prompting user for input - USERNAME/PASSWORD FILE
# user_file _ in__("\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")
#
# #Verifying the validity of the USERNAME/PASSWORD file
# __ __.pa__.i_f.. ? __ T..
#     print("\n* Username/password file is valid :)\n")
#
# ____
#     print("\n* File # does not exist :( Please check and try again.\n".f.. ?
#     ___.e..
#
# #Checking commands file
# #Prompting user for input - COMMANDS FILE
# cmd_file _ in__("\n# Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")
#
# #Verifying the validity of the COMMANDS FILE
# __ __.pa__.i_f.. ? __ T..
#     print("\n* Command file is valid :)\n")
#
# ____
#     print("\n* File # does not exist :( Please check and try again.\n".f.. ?
#     ___.e..
#
# #Open SSHv2 connection to the device
# ___ ssh_connection ip
#
#     g.. u..
#     g.. c..
#
#     #Creating SSH CONNECTION
#     ___
#         #Define SSH parameters
#         selected_user_file _ o.. ? _
#
#         #Starting from the beginning of the file
#         ?.s.. 0
#
#         #Reading the username from the file
#         username _ ?.r_l.. 0 .sp.. ',' 0 .rs.. "\n"
#
#         #Starting from the beginning of the file
#         ?.s.. 0
#
#         #Reading the password from the file
#         p__swor. _ ?.r_l.. 0 .sp.. ',' 1 .rs.. "\n"
#
#         #Logging into device
#         session _ ?.S..
#
#         #For testing purposes, this allows auto-accepting unknown host keys
#         #Do not use in production! The default would be RejectPolicy
#         ?.s_m_h_k_p.. ?.A..
#
#         #Connect to the device using username and password
#         ?.c.. ip.rs.. "\n" u.. _ u.. p__swor. _ p__swor.
#
#         #Start an interactive shell session on the router
#         connection _ ?.i_s..
#
#         #Setting terminal length for entire output - disable pagination
#         ?.s..("enable\n")
#         ?.s..("terminal length 0\n")
#         t__.s.. 1
#
#         #Entering global config mode
#         ?.s.. "\n"
#         c__.s..("configure terminal\n")
#         t__.s.. 1
#
#         #Open user selected file for reading
#         selected_cmd_file _ o.. c.. _
#
#         #Starting from the beginning of the file
#         ?.s.. 0
#
#         #Writing each line in the file to the device
#         ___ each_line __ ?.r_l..
#             c__.s.. ? + '\n')
#             t__.s.. 2
#
#         #Closing the user file
#         ?.c..
#
#         #Closing the command file
#         ?.c..
#
#         #Checking command output for IOS syntax errors
#         router_output _ c__.r.. 65535
#
#         __ __.s.. _"@ Invalid input" ?
#             print("* There was at least one IOS syntax error on device # :(".f.. ?
#
#         ____
#             print("\nDONE for device @ :)\n".f.. ?
#
#         #Test for reading command output
#         print st. ? + "\n")
#
#         #Closing the connection
#         s__.c..
#
#     ______ ?.A..
#         print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
#         print("* Closing program... Bye!")