# The concrete path classes include a resolve() method for normalizing a path by looking at the filesystem for directories and symbolic links and producing the absolute path referred to by a name.

# pathlib_resolve.py

import pathlib

usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(share.resolve())

# Here the relative path is converted to the absolute path to /usr/share. If the input path includes symlinks, those are expanded as well to allow the resolved path to refer directly to the target.
#
# $ python3 pathlib_resolve.py
#
# /usr/share