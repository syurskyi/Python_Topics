# The Python Standard Library also supports creating TAR and ZIP archives using the high-level methods
# in the shutil module. The archiving utilities in shutil allow you to create, read, and extract ZIP and TAR archives.
# These utilities rely on the lower level tarfile and zipfile modules.
#
# Working With Archives Using shutil.make_archive()
# shutil.make_archive() takes at least two arguments: the name of the archive and an archive format.
# By default, it compresses all the files in the current directory into the archive format specified
# in the format argument. You can pass in an optional root_dir argument to compress files in
# a different directory. .make_archive() supports the zip, tar, bztar, and gztar archive formats.
#
# This is how to create a TAR archive using shutil:
#
# import shutil
#
# # shutil.make_archive(base_name, format, root_dir)
# shutil.make_archive('data/backup', 'tar', 'data/')
#
# This copies everything in data/ and creates an archive called backup.tar in the filesystem and returns its name.
# To extract the archive, call .unpack_archive():
#
# shutil.unpack_archive('backup.tar', 'extract_dir/')
#
# Calling .unpack_archive() and passing in an archive name and destination directory extracts the contents
# of backup.tar into extract_dir/. ZIP archives can be created and extracted in the same way.

