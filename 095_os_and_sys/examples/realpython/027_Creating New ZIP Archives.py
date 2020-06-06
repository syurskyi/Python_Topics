# To create a new ZIP archive, you open a ZipFile object in write mode (w) and add the files you want to archive:
#
# >>> import zipfile
#
# >>> file_list = ['file1.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
# >>> with zipfile.ZipFile('new.zip', 'w') as new_zip:
# ...     for name in file_list:
# ...         new_zip.write(name)
#
# In the example, new_zip is opened in write mode and each file in file_list is added to the archive.
# When the with statement suite is finished, new_zip is closed. Opening a ZIP file in write mode erases
# the contents of the archive and creates a new archive.
#
# To add files to an existing archive, open a ZipFile object in append mode and then add the files:
#
# >>> # Open a ZipFile object in append mode
# >>> with zipfile.ZipFile('new.zip', 'a') as new_zip:
# ...     new_zip.write('data.txt')
# ...     new_zip.write('latin.txt')
#
# Here, you open the new.zip archive you created in the previous example in append mode. Opening the ZipFile object
# in append mode allows you to add new files to the ZIP file without deleting its current contents.
# After adding files to the ZIP file, the with statement goes out of context and closes the ZIP file.