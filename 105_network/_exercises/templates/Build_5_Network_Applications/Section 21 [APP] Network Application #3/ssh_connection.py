# ______ pa..
# ______ d_t_
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
# __ __.pa__.i_f..(?) __ T..
#     print("\n* Username/password file is valid :)\n")
#
# ____
#     print("\n* File @ does not exist :( Please check and try again.\n".f.. ?
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
#     print("\n* File @ does not exist :( Please check and try again.\n".f.. ?
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
#         password _ ?.r_l.. 0 .sp.. ',' 1 .rs.. "\n"
#
#         #Logging into device
#         session _ ?.S..
#
#         #For testing purposes, this allows auto-accepting unknown host keys
#         #Do not use in production! The default would be RejectPolicy
#         ?.s_m_h_k_p.. ?.AAP..
#
#         #Connect to the device using username and password
#         ?.c.. i_.rs.. "\n" us.. _ u.. p__. _ p__
#
#         #Start an interactive shell session on the router
#         connection _ ?.i_s..
#
#         #Setting terminal length for entire output - disable pagination
#         ?.s.. "enable\n"
#         ?.s.. "terminal length 0\n"
#         t__.s.. 1
#
#         #Entering global config mode
#         ?.s.. "\n"
#         ?.s.. "configure terminal\n"
#         t__.s.. 1
#
#         #Open user selected file for reading
#         selected_cmd_file _ o.. c_f.. _
#
#         #Starting from the beginning of the file
#         ?.s.. 0
#
#         #Writing each line in the file to the device
#         ___ each_line __ ?.r_l..
#             ?.s.. ? + '\n'
#             t__.s.. 2
#
#         #Closing the user file
#         s_u_f__.c..
#
#         #Closing the command file
#         ?.c..
#
#         #Checking command output for IOS syntax errors
#         router_output _ ?.r.. 65535
#
#         __ __.s.. _"@ Invalid input" ?
#             print("* There was at least one IOS syntax error on device @ :(".f.. ?
#
#         ____
#             print("\nDONE for device @. Data sent to file at @.\n".f.. ? st. d_t_.d_t_.n..
#
#         #Test for reading command output
#         #print(str(router_output) + "\n")
#
#         #Searching for the CPU utilization value within the output of "show processes top once"
#         cpu _ __.s.. _"%Cpu\(s\):(\s)+(.+?)(\s)* us," ?
#
#         #Extracting the second group, which matches the actual value of the CPU utilization and decoding to the UTF-8 format from the binary data type
#         utilization _ ?.g.. 2 .d.. "utf-8"
#
#         #Printing the CPU utilization value to the screen
#         #print(utilization)
#
#         #Opening the CPU utilization text file and appending the results
#         w__ o.. "D:\\App3\\cpu.txt" _ __ f
#             #f.write("{},{}\n".format(str(datetime.datetime.now()), utilization))
#             f.w.. u.. + "\n")
#
#         #Closing the connection
#         s__.c..
#
#     ______ ?.A..
#         print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
#         print("* Closing program... Bye!")