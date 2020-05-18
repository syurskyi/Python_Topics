# ______ _3
#
# # Summary: in this tutorial, we will show you step by step how to query data in SQLite from Python.
# #
# # To query data in an SQLite database from Python, you use these steps:
# #
# #     First, establish a connection to the SQLite database by creating a Connection object.
# #     Next, create a Cursor object using the cursor method of the Connection object.
# #     Then, execute a  S.. statement.
# #     After that, call the f_a.. method of the cursor object to fetch the data.
# #     Finally, loop the cursor and process each row individually.
# #
# # In the following example, we will use the tasks table created in the creating tables tutorial.
#
# # First, create a connect to an SQLite database specified by a file:
#
# ___ create_connection db_file
#     """ create a database connection to the SQLite database
#         specified by the db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn_ N..
#     ____
#         conn_ _3.c.. ?
#     ______ E.. __ e
#         print ?
#
#     r_ ?
#
# # This function selects all rows from the tasks table and display the data:
#
# ___ select_all_tasks conn
#     """
#     Query all rows in the tasks table
#     :param conn: the Connection object
#     :return:
#     """
#     cur_ ?.c..
#     ?.e.. S.. _ F.. tasks
#
#     rows_ ?.f..
#
#     ___ row __ ?
#         print ?
#
# # In the select_all_tasks() function, we created a cursor, executed the S.. statement,
# # and called the  f_a.. to fetch all tasks from the tasks table.
# #
# # This function query tasks by priority:
#
# ___ select_task_by_priority conn priority
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur_ ?.c..
#     ?.e.. S... _ F.. tasks W.. priority_? p..
#
#     rows_ ?.f..
#
#     ___ row __ ?
#         print ?
#
# # In the select_task_by_priority() function, we selected the tasks based on a particular priority.
# # The question mark ( ?) in the query is the placeholder. When the cursor executed the S.. statement,
# # it substituted the question mark ( ?) by the priority argument. The  f_a.. method fetched all matching tasks
# # by the priority.
# #
# # This main() function creates a connection to the database
# # C:\sqlite\db\pythonsqlite.db and calls the functions to query all rows from the tasks table and select tasks
# # with priority 1:
#
#
# ___ main
#     database_ "pythonsqlite.db"
#
#     # create a database connection
#     conn_ c_c.. ?
#     w___ ?
#         print("1. Query task by priority:")
#         s_t_b_p.. ? 1
#
#         print("2. Query all tasks")
#         s_a_t.. ?
#
#
# __ _______ __ _____
#     ?
