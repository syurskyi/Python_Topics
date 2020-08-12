
from .Path ______ Path

from .FileObject ______ FileObject

class InvalidFileObject(FileObject):
    '''When we get a path that doesn't actually point to areadl object'''


    @property
    ___ is_file(self):
        return False


    @property
    ___ is_dir(self):
        return False
