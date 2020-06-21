# ______ ma__.pyp.. __ pyp
# ______ ma__.ani.. __ animation
#
# #Creating a new figure
# figure _ ?.fi..
#
# #Creating a subplot with 1 row, 1 column and index 1 - this means a single subplot in our figure
# subplot _ ?.a_su..  1, 1, 1
#
# #Creating the function that reads the data from cpu.txt and feeds it to our subplot
# ___ animation_function i
#     #Opening the file and reading each row of CPU utilization data in the file; creating a list of values
#     cpu_data _ o.. "D:\\App3\\cpu.txt" .r_l..
#
#     #Creating an empty list in which to append each value in the file converted from string to float;
#     x _   # list
#
#     #Iterating over the list of CPU values and appending each value (converted to float) to the previously created list - x; adding an if statement to exclude any blank lines in the file
#     ___ each_value __ ?
#         __ le. ? > 1
#             x.ap.. fl.. ?
#
#     #Clearing/refreshing the figure to avoid unnecessary overwriting for each new poll (every 10 seconds)
#     ?.cl..
#
#     #Plotting the values in the list
#     ?.pl.. x
#
# #Using the figure, the function and a polling interval of 10000 ms (10 seconds) to build the graph
# graph_animation _ ?.FA.. f.. a_f.. i.. _ 10000)
#
# #Displaying the graph to the screen
# ?.sh..