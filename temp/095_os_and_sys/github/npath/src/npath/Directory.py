from .Path ______ Path

from .FileObject ______ FileObject

class Directory(FileObject):


    @property
    def is_file(self):
        return False


    @property
    def is_dir(self):
        return True


    @property
    def parent(self):
        return self.FILE_OBJ_FACTORY(self.parent)


    @property
    def files(self):
        for path in self.files:
            yield self.FILE_OBJ_FACTORY(path)


    @property
    def dirs(self):
        for path in self.dirs:
            yield self.FILE_OBJ_FACTORY(path)


    @property
    def all(self):
        for o in self.files:
            yield o
        for o in self.dirs:
            yield o


    def walk(self):
        '''
        Return all file objects under a given path recursively

        All paths are made relative to this directory.

        :return: FileObject (File, Directory, UnknownFileObject)
        '''
        for path in super(Directory, self).walk():
            yield self.FILE_OBJ_FACTORY(path.make_relative_to(self))


    def find(self, files_None, dirs_None):
        for child in self.walk():
            if child.is_file:
                if files is None or files is True:
                    yield child
            elif child.is_dir:
                if dirs is None or dirs is True:
                    yield child
