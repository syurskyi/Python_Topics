____ .Path ______ Path

____ .FileObject ______ FileObject

c_ Directory(FileObject):


    @property
    ___ is_file
        r_ F..


    @property
    ___ is_dir
        r_ T..


    @property
    ___ parent
        r_ FILE_OBJ_FACTORY(parent)


    @property
    ___ files
        ___ path __ files:
            yield FILE_OBJ_FACTORY(path)


    @property
    ___ dirs
        ___ path __ dirs:
            yield FILE_OBJ_FACTORY(path)


    @property
    ___ all
        ___ o __ files:
            yield o
        ___ o __ dirs:
            yield o


    ___ walk
        '''
        Return all file objects under a given path recursively

        All paths are made relative to this directory.

        :return: FileObject (File, Directory, UnknownFileObject)
        '''
        ___ path __ s___(Directory, ).walk():
            yield FILE_OBJ_FACTORY(path.make_relative_to())


    ___ find(, files_None, dirs_None):
        ___ child __ walk():
            __ child.is_file:
                __ files __ N.. or files __ T..:
                    yield child
            ____ child.is_dir:
                __ dirs __ N.. or dirs __ T..:
                    yield child
