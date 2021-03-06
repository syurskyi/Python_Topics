# # To create a new ZIP archive, you open a ZipFile object in write mode (w) and add the files you want to archive:
#
# ______ z_f_
#
# file_list _  'file1.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py'
# w__ z_f_.ZF.. 'new.zip' _ __ new_zip
#     ___ name __ ?
#         ?.w.. ?
#
# # In the example, new_zip is opened in write mode and each file in file_list is added to the archive.
# # When the with statement suite is finished, new_zip is closed. Opening a ZIP file in write mode erases
# # the contents of the archive and creates a new archive.
# #
# # To add files to an existing archive, open a ZipFile object in append mode and then add the files:
# #
# # Open a ZipFile object in append mode
# w__ z_f_.ZF.. 'new.zip' _ __ new_zip
#     ?.w.. 'data.txt'
#     ?.w.. 'latin.txt'
#
# # Here, you open the new.zip archive you created in the previous example in append mode. Opening the ZipFile object
# # in append mode allows you to add new files to the ZIP file without deleting its current contents.
# # After adding files to the ZIP file, the with statement goes out of context and closes the ZIP file.