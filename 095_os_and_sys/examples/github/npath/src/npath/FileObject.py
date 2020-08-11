from abc import ABCMeta, abstractmethod, abstractproperty

from . import Path


class FileObject(Path):
    FILE_OBJ_FACTORY = None # set in __init__.py


    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.__path)

    @property
    def path(self):
        '''Return path to file object as a Path (not normally needed)'''
        return Path(self)


    @abstractproperty
    def is_file(self):
        '''Is this a file object'''


    @abstractproperty
    def is_dir(self):
        '''Is this a directory object'''


    @property
    def isfile(self):
        return self.is_file


    @property
    def isdir(self):
        return self.is_dir


