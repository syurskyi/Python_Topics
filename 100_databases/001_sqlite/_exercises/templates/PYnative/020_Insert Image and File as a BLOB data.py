# _____ ?
#
# ___ convertToBinaryData filename
#     #Convert digital data to binary format
#     w__ o.. ? __ __ file
#         blobData _ ?.r..
#     r_ ?
#
# ___ insertBLOB empId name photo resumeFile
#     ___
#         sqliteConnection _ ?.c.. 'SQLite_Python.db'
#         cursor _ ?.c..
#         print("Connected to SQLite")
#         sqlite_insert_blob_query _ """ I.. I.. new_employee
#                                   (id, name, photo, resume) V.. _ _ _ _"""
#
#         empPhoto _ ? p..
#         resume _ ? r..
#         # Convert data into tuple format
#         data_tuple _ ? ? ? ?
#         ?.e.. ? ?
#         ?.c..
#         print("Image and file inserted successfully as a BLOB into a table")
#         ?.c..
#
#     _____ ?.E.. __ error
#         print("Failed to insert blob data into sqlite table" ?
#     f..
#         __ (?
#             ?.c..
#             print("the sqlite connection is closed")
#
# ? 1 "Smith", "E:\pynative\Python\photos\smith.jpg", "E:\pynative\Python\photos\smith_resume.txt"
# ? 2 "David", "E:\pynative\Python\photos\david.jpg", "E:\pynative\Python\photos\david_resume.txt"
#
#
# # Output:
# #
# # Connected to SQLite
# # Image and file inserted successfully as a BLOB into a table
# # the sqlite connection is closed
# # Connected to SQLite
# # Image and file inserted successfully as a BLOB into a table
# # the sqlite connection is closed