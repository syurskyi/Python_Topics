# _____ ?
#
# ___ readSqliteTable
#     ___
#         sqliteConnection _ ?.c.. 'SQLite_Python.db'
#         cursor _ ?.c..
#         print("Connected to SQLite")
#
#         sqlite_select_query _ """S.. _ f.. SqliteDb_developers"""
#         ?.e.. ?
#         records _ ?.f_a..
#         print("Total rows are:  ", le. ?
#         print("Printing each row")
#         ___ row __ records
#             print("Id: " ? 0
#             print("Name: " ? 1
#             print("Email: " ?[2
#             print("JoiningDate: " ? 3
#             print("Salary: " ? 4
#             print("\n")
#
#         ?.c..
#
#     _____ ?.E.. __ error
#         print("Failed to read data from sqlite table" ?
#     f..
#         __ (?
#             ?.c..
#             print("The SQLite connection is closed")
#
# ?
#
#
# # Output:
# #
# # C:\Anaconda3\envs\demos\python.exe E:/demos/sqlite_demos/sqlite_select.py
# # Connected to SQLite
# # Total rows are:   6
# #
# # Printing each row
# # Id:  1
# # Name:  James
# # Email:  james@pynative.com
# # JoiningDate:  2019-03-17
# # Salary:  8000.0
# #
# # Id:  2
# # Name:  Joe
# # Email:  joe@pynative.com
# # JoiningDate:  2019-05-19
# # Salary:  9000.0
# #
# # Id:  3
# # Name:  Ben
# # Email:  ben@pynative.com
# # JoiningDate:  2019-02-23
# # Salary:  9500.0
# #
# # Id:  4
# # Name:  Jos
# # Email:  jos@gmail.com
# # JoiningDate:  2019-01-14
# # Salary:  9500.0
# #
# # Id:  5
# # Name:  Chris
# # Email:  chris@gmail.com
# # JoiningDate:  2019-05-15
# # Salary:  7600.0
# #
# # Id:  6
# # Name:  Jonny
# # Email:  jonny@gmail.com
# # JoiningDate:  2019-03-27
# # Salary:  8400.0
# #
# # The SQLite connection is closed