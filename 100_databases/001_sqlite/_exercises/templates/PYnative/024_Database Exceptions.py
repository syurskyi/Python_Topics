# _____ ?
# _____ tr..
# _____ ___
#
# ___
#     sqliteConnection _ ?.c.. 'SQLite_Python.db'
#     cursor _ ?.c..
#     print("Successfully Connected to SQLite")
#
#     sqlite_insert_query _ """I.. I.. unknown_table_1
#                           (id, text)  V..  (1, 'Demo Text')"""
#
#     count _ ?.e.. ?
#     ?.c..
#     print("Record inserted successfully into SqliteDb_developers table " ?.r..
#     ?.c..
#
# _____ ?.E.. __ error
#     print("Failed to insert data into sqlite table")
#     print("Exception class is: " ?. -c
#     print("Exception is" ?.a..
#     print('Printing detailed SQLite exception traceback: ')
#     _t.. _v.. _t. _ ___.e_i..
#     print ?.f_e.. ? ? ?
# f..
#     __ (?
#         ?.c..
#         print("The SQLite connection is closed")
#
#
# # Output:
# #
# # Successfully Connected to SQLite
# # Failed to insert data into sqlite table
# # Exception class is:  <class '?.OperationalError'>
# # Exception is ('no such table: unknown_table_1',)
# # Printing detailed SQLite exception traceback:
# # ['Traceback (most recent call last\n', '  File "E:/demos/sqlite_demos/sqlite_errors.py", line 13, in <module>\n    count = cursor.execute(sqlite_insert_query)\n', '?.OperationalError: no such table: unknown_table_1\n']
# # The SQLite connection is closed