from abc ______ ABCMeta, abstractmethod, abstractproperty

from . ______ Path


class FileObject(Path):
    FILE_OBJ_FACTORY _ None # set in __init__.py


    ___ __repr__(self):
        return "%s('%s')" % (self.__class__. -n, self.__path)

    @property
    ___ path(self):
        '''Return path to file object as a Path (not normally needed)'''
        return Path(self)


    @abstractproperty
    ___ is_file(self):
        '''Is this a file object'''


    @abstractproperty
    ___ is_dir(self):
        '''Is this a directory object'''


    @property
    ___ isfile(self):
        return self.is_file


    @property
    ___ isdir(self):
        return self.is_dir


