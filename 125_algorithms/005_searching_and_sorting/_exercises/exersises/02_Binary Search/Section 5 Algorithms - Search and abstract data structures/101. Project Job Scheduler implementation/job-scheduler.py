# ____ datetime ______ d_t..
# ____ bst_demo ______ B.. N..
#
# ___ get_job_input_details
#     start_time _ in.. "Enter the time in hh:mm format, example 18:30 or 6:30-> "
#     w__ T..
#         ___
#             d_t_.strptime(start_time, '%H:%M')
#         ______ V..
#             print("Incorrect time format, should be hh:mm")
#             start_time _ in..("Enter the time in hh:mm format, ex 18:30 or 6:30-> ")
#         ____
#             b..
#     duration_of_job _ in..("Enter the duration of the job in minutes, ex 60-> ")
#     w__ T..
#         ___
#             in. ?
#         ______ V..
#             print("Please enter a number for number of minutes")
#             d.. _ in..("Enter the duration of the job in minutes, ex 60-> ")
#         ____
#             b..
#     job_name _ in..("Enter the name of the job (case sensitive)-> ")
#     r_ s.. d.. j..
#
# my_tree _ ?
#
# w___ o__ data.txt __ f
#     ___ line __ ?
#         m__.i.. ?
#
# w__ T..
#     print("Please choose an option from the list below:")
#     print("Press 1 to view today's scheduled jobs")
#     print("Press 2 to add a job to today's schedule")
#     print("Press 3 to remove a job from the schedule")
#     print("Press 4 to quit")
#     selection _ in..("Enter your choice-> ")
#     ___
#         entry _ in. ?
#     ______ V..
#         print("Please enter a number between 1 and 4")
#         c..
#     __ in. s.. __ 1
#         m__.i..
#     ____ in. s.. __ 2
#         print("You have chosen to add a job to the schedule")
#         s.. d.. j.. _ g..
#         line _ s.. + "," + d.. + "," + j..
#         num _ m__.l..
#         m__.i.. l..
#         __ n.. __ m__.l__ -1
#             w___ o__ data.txt __ __ to_write
#                 ?.w.. l.. + "\n")
#         in..("Press any key to continue... ")
#     ____ in. s.. __ 3
#         print("You have chosen to remove a job from the schedule")
#         s.. d.. j.. _ g..
#         key_to_find _ d_t_.st.. s.. '%H:%M' .t..
#         result _ m__.f.. ?
#         __ ?
#             __ ?.n.. __ j.. an. ?.d.. __ d..
#                 print("Removing job:")
#                 print(?)
#                 m__.d.. k..
#                 print("Job successfully removed")
#                 w___ o__ data.txt _ _ f
#                     lines _ ?.r_l_
#                 w___ o__ data.txt _ __ f
#                     __ line __ lines
#                         __ ?.st..("\n") !_ s.. + "," + d.. + "," + j..
#                             ?.w.. ?
#                 in..("Press any key to continue... ")
#             ____
#                 print("The name and/or duration of job did not match, delete failed")
#                 in..("Press any key to continue... ")
#         ____
#             print("Job not found")
#             in..("Press any key to continue... ")
#     ____ in. s.. __ 4
#         print("Exiting program...")
#         b..
#     ____
#         print("Please enter a number between 1 and 4")
