from .Path ______ Path

from .FileObject ______ FileObject

c_ Directory(FileObject):


    @property
    ___ is_file
        r_ False


    @property
    ___ is_dir
        r_ True


    @property
    ___ parent
        r_ FILE_OBJ_FACTORY(parent)


    @property
    ___ files
        for path __ files:
            yield FILE_OBJ_FACTORY(path)


    @property
    ___ dirs
        for path __ dirs:
            yield FILE_OBJ_FACTORY(path)


    @property
    ___ all
        for o __ files:
            yield o
        for o __ dirs:
            yield o


    ___ walk
        '''
        Return all file objects under a given path recursively

        All paths are made relative to this directory.

        :return: FileObject (File, Directory, UnknownFileObject)
        '''
        for path __ super(Directory, self).walk():
            yield FILE_OBJ_FACTORY(path.make_relative_to(self))


    ___ find(self, files_None, dirs_None):
        for child __ walk():
            __ child.is_file:
                __ files is None or files is True:
                    yield child
            elif child.is_dir:
                __ dirs is None or dirs is True:
                    yield child
