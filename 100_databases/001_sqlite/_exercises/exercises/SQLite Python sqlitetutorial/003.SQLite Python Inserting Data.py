# ______ _3
# # First, create a new function to establish a database connection to an SQLitte database specified by the database file.
#
# ___ create_connection db_file
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn _ N..
#     ___
#         conn _ _3.c.. ?
#     ______ E.. __ e
#         print ?
#
#     r_ ?
#
# # Next, develop a function to insert a new project into the projects table.
#
# ___ create_project conn project
#     """
#     Create a new project into the projects table
#     :param conn:
#     :param project:
#     :return: project id
#     """
#     sql _  I.. I.. projects|n.. b_d.. e_d..
#               V.. _ _ _
#     cur _ ?.c..
#     ?.e.. s.. p..
#     r_ ?.l..
#
# # In this function, we used the  lastrowid attribute of the Cursor object to get back the generated id.
# #
# # Then, develop another function for inserting rows into the tasks table.
#
#
# ___ create_task conn task
#     """
#     Create a new task
#     :param conn:
#     :param task:
#     :return:
#     """
#
#     sql _  I.. I.. tasks|n.. p.. s_i. p_i. b_d.. e_d..
#               V.. _ _ _ _ _ _
#     cur _ ?.c..
#     ?.e.. s.. t..
#     r_ ?.l..
#
# # After that, develop the main() function that creates a new project and two tasks associated with the project.
#
#
# ___ main
#     database _ pythonsqlite.db
#
#     # create a database connection
#     conn _ c_c.. ?
#     w___ ?
#         # create a new project
#         project _ ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
#         project_id _ c_p.. c.. p..
#
#         # tasks
#         task_1 _ ('Analyze the requirements of the app', 1, 1, p_i. '2015-01-01', '2015-01-02')
#         task_2 _ ('Confirm with user about the top requirements', 1, 1, p_i. '2015-01-03', '2015-01-05')
#
#         # create tasks
#         c_t.. c.. _1
#         c_t.. c.. _2
#
#
# __ _______ __ _____
#     ?
