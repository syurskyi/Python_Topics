# _____ ?
# _____ d_t_
#
# ___ addDeveloper id name joiningDate
#     ___
#         sqliteConnection _ ?.c..'SQLite_Python.db'
#                                            detect_types_?.P_D.. _
#                                            ?.P_C..
#         cursor _ ?.c..
#         print("Connected to SQLite")
#
#         sqlite_create_table_query _ '''C.. T.. new_developers (
#                                        id I.. P.. K..,
#                                        name T.. N.. N..,
#                                        joiningDate timestamp);'''
#
#         ? _ ?.c..
#         ?.e.. ?
#
#         # insert developer detail
#         sqlite_insert_with_param _ """I.. I.. 'new_developers'
#                           ('id', 'name', 'joiningDate')
#                           V.. _ _ _;"""
#
#         data_tuple _ ? ? ?
#         ?.e.. ? ?
#         ?.c..
#         print("Developer added successfully \n")
#
#         # get developer detail
#         sqlite_select_query _ """S.. name, joiningDate f.. new_developers w.. id = ?"""
#         ?.e.. ? 1
#         records _ ?.f_a..
#
#         ___ row __ ?
#             developer_ ? 0
#             joining_Date _ ? 1
#             print d.. " joined on" ?
#             print("joining date type is" ty.. ?
#
#         ?.c..
#
#     _____ ?.E.. __ error
#         print("Error while working with SQLite" ?
#     f..
#         __ (?
#             ?.c..
#             print("sqlite connection is closed")
#
# ? 1, 'Mark', d_t_.d_t_.n..
#
#
# # Output:
# #
# # Connected to SQLite
# # Developer added successfully
# #
# # Mark  joined on 2019-06-28 20:57:32.352790
# # joining date type is <class 'datetime.datetime'>
# # sqlite connection is closed