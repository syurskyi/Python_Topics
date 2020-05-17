# # First, develop a function called create_connection() that returns a Connection object which represents an SQLite
# # database specified by the database file parameter db_file.
#
# ______ _3
#
# ___ create_connection db_file
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn _ N..
#     ___
#         ? _ _3.c.. ?
#         r_ ?
#     ______ E.. __ e
#         print ?
#
#     r_ ?
#
# # Second, develop a function named create_table() that accepts a Connection object and an SQL statement.
# # Inside the function, we call the execute() method of the Cursor object to execute the C.. T.. statement.
#
# ___ create_table conn create_table_sql
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a C.. T.. statement
#     :return:
#     """
#     ___
#         c _ ?.c..
#         ?.e.. ?
#     ______ E.. __ e
#         print >
#
# # Third, create a main() function to create the  projects and tasks tables.
#
# ___ main
#     database _ "pythonsqlite.db"
#
#     sql_create_projects_table _  C... T.. I. N.. E.. projects (
#                                         id int.. PR.. K..
#                                         name te.. N.. N...
#                                         begin_date te..
#                                         end_date te..
#                                     );
#
#     sql_create_tasks_table _ C.. T.. I. NO. E.. tasks (
#                                     i. int.. P.. K..
#                                     name te.. N.. N..
#                                     priority int..
#                                     status_id int.. N.. N..
#                                     project_id int.. N.. N..
#                                     begin_date te.. N.. N..
#                                     end_date te.. N.. N..
#                                     F.. K.. |p_i. RE.. projects |i.
#                                 );
#
#     # create a database connection
#     conn _ c_c.. d..
#
#     # create tables
#     __ ? __ no. N..
#         # create projects table
#         c_t.. ? s_c_p_t..
#
#         # create tasks table
#         c_t.. ? s_c_t_t..
#     ____
#         print("Error! cannot create the database connection.")
#
#
# __ _______ __ _____
#     ?
