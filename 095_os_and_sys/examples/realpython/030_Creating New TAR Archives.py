# Here’s how you do it:
#
# >>> import tarfile
#
# >>> file_list = ['app.py', 'config.py', 'CONTRIBUTORS.md', 'tests.py']
# >>> with tarfile.open('packages.tar', mode='w') as tar:
# ...     for file in file_list:
# ...         tar.add(file)
#
# >>> # Read the contents of the newly created archive
# >>> with tarfile.open('package.tar', mode='r') as t:
# ...     for member in t.getmembers():
# ...         print(member.name)
# app.py
# config.py
# CONTRIBUTORS.md
# tests.py
#
# First, you make a list of files to be added to the archive so that you don’t have to add each file manually.
# The next line uses the with context manager to open a new archive called packages.tar in write mode.
# Opening an archive in write mode('w') enables you to write new files to the archive.
# Any existing files in the archive are deleted and a new archive is created.
# After the archive is created and populated, the with context manager automatically closes it and saves
# it to the filesystem. The last three lines open the archive you just created and print out the names of the files
# contained in it.
#
# To add new files to an existing archive, open the archive in append mode ('a'):
#
# >>> with tarfile.open('package.tar', mode='a') as tar:
# ...     tar.add('foo.bar')
#
# >>> with tarfile.open('package.tar', mode='r') as tar:
# ...     for member in tar.getmembers():
# ...         print(member.name)
# app.py
# config.py
# CONTRIBUTORS.md
# tests.py
# foo.bar
#
# Opening an archive in append mode allows you to add new files to it without deleting the ones already in it.