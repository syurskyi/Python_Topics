# _____ ?
#
# ___ _toTileCase string
#     r_ st. ?.ti..
#
# ___ getDeveloperName id
#     ___
#         sqliteConnection _ ?.c.. 'SQLite_Python.db'
#         cursor _ ?.c..
#         print("Connected to SQLite")
#
#         ?.create_function "TOTILECASE" 1 _?
#         select_query _ "S.. T..(name) F.. SqliteDb_developers w.. id = ?"
#         ?.e.. ? ?
#         name _ ?.f_o..
#         print("Developer Name is" ?
#         ?.c..
#
#     _____ ?.E.. __ error
#         print("Failed to read data from sqlite table" ?
#     f..
#         __ (?
#             ?.c..
#             print("sqlite connection is closed")
#
# ? 2
#
# # Output:
# #
# # Connected to SQLite
# # Developer Name is ('Joe',)
# # sqlite connection is closed