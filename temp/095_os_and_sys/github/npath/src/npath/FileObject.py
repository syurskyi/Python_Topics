____ abc ______ ABCMeta, abstractmethod, abstractproperty

____ . ______ Path


c_ FileObject(Path):
    FILE_OBJ_FACTORY _ N.. # set in __init__.py


    ___ __repr__
        r_ "%s('%s')" % ( -c . -n, __path)

    @property
    ___ path
        '''Return path to file object as a Path (not normally needed)'''
        r_ Path()


    @abstractproperty
    ___ is_file
        '''Is this a file object'''


    @abstractproperty
    ___ is_dir
        '''Is this a directory object'''


    @property
    ___ isfile
        r_ is_file


    @property
    ___ isdir
        r_ is_dir


