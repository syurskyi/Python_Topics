# _____ ?
#
# ___ readLimitedRows rowSize
#     ___
#         sqliteConnection _ ?.c..('SQLite_Python.db')
#         cursor _ ?.c..
#         print("Connected to SQLite")
#
#         sqlite_select_query _ """S.. _ f.. SqliteDb_developers"""
#         ?.e.. ?
#         print("Reading " ? " rows")
#         records _ ?.f_m.. ?
#         print("Printing each row \n")
#         ___ row __ ?
#             print("Id: " ? 0
#             print("Name: " ? 1
#             print("Email: " ? 2
#             print("JoiningDate: " ? 3
#             print("Salary: " ? 4
#             print("\n")
#
#         ?.c..
#
#     _____ ?.E.. __ error:
#         print("Failed to read data from sqlite table" ?
#     f..
#         __ (?
#             ?.c..
#             print("The SQLite connection is closed")
#
# ? 2
#
# # Output:
# #
# # Connected to SQLite
# # Reading 2  rows
# # Printing each row
# #
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
# # The SQLite connection is closed