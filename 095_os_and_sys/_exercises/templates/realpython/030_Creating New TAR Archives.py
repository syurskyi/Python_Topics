# # Here’s how you do it:
#
# ______ t_f_
#
# file_list _ 'app.py', 'config.py', 'CONTRIBUTORS.md', 'tests.py'
# w__ t_f_.o.. 'packages.tar' m.. _ _ __ ta_
#     ___ file __ ?
#         ta_.a.. ?
#
# # Read the contents of the newly created archive
# w__ t_f_.o.. 'package.tar' m.._ _ __ t
#     ___ member __ ?.g_m..
#         print ?.n..
#
# # app.py
# # config.py
# # CONTRIBUTORS.md
# # tests.py
# #
# # First, you make a list of files to be added to the archive so that you don’t have to add each file manually.
# # The next line uses the with context manager to open a new archive called packages.tar in write mode.
# # Opening an archive in write mode('w') enables you to write new files to the archive.
# # Any existing files in the archive are deleted and a new archive is created.
# # After the archive is created and populated, the with context manager automatically closes it and saves
# # it to the filesystem. The last three lines open the archive you just created and print out the names of the files
# # contained in it.
# #
# # To add new files to an existing archive, open the archive in append mode ('a'):
#
# w__ t_f_.o.. 'package.tar' m.._ _ __ ta_
#     ta_.a.. 'foo.bar'
#
# w__ t_f_.o.. 'package.tar' m.._ _ __ ta_
#    ___ member __ ta_.g_m..
#        print ?.n..
#
# # app.py
# # config.py
# # CONTRIBUTORS.md
# # tests.py
# # foo.bar
# #
# # Opening an archive in append mode allows you to add new files to it without deleting the ones already in it.