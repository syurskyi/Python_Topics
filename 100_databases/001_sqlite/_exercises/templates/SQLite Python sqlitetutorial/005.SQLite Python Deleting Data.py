# # Summary: this tutorial shows you how to delete data in the SQLite database
# # from a Python program using the _3 module.
# #
# # In order to delete data in the SQLite database from a Python program, you use the following steps:
# #
# #     First, establish a connection the SQLite database by creating a Connection object using the connect() function.
# #     Second, to execute a D.. statement, you need to create a Cursor object using the cursor()
# #     method of the Connection object.
# #     Third, execute the  D.. statement using the execute() method of the Cursor object.
# #     In case you want to pass the arguments to the statement, you use a question mark ( ?) for each argument.
# #
# # The following  create_connection() function establishes a database connection to an SQLite database
# # specified by a database file name:
#
# ______ _3
#
#
# ___ create_connection db_file
#     """ create a database connection to the SQLite database
#         specified by the db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn _ N..
#     ___
#         ? _ _3.c.. ?
#     _____ E.. __ e
#         print ?
#
#     r_ ?
#
# # The following delete_task() function deletes a task in the tasks table by id.
#
# ___ delete_task conn id
#     """
#     Delete a task by task id
#     :param conn:  Connection to the SQLite database
#     :param id: id of the task
#     :return:
#     """
#     sql _  D.. F.. tasks W.. i._?'
#     cur _ ?.c..
#     ?.e.. s.. i.,
#     ?.c..
#
# # The following delete_all_tasks() function deletes all rows in the tasks table.
#
#
# ___ delete_all_tasksconn
#     """
#     Delete all rows in the tasks table
#     :param conn: Connection to the SQLite database
#     :return:
#     """
#     sql _ 'D.. F.. tasks'
#     cur _ ?.c..
#     ?.e.. s..
#     ?.c..
#
#
# ___ main
#     database _ "pythonsqlite.db"
#
#     # create a database connection
#     conn _ c_c.. ?
#     w___ ?
#         d_t.. ? 2
#         # delete_all_tasks(conn);
#
#
# __ _______ __ _____
#     ?
