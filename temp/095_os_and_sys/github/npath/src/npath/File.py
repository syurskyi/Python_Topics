______ os
______ hashlib

from .Path ______ Path

from .FileObject ______ FileObject

class File(FileObject):

    @property
    def is_file(self):
        return True


    @property
    def is_dir(self):
        return False


    @property
    def size(self):
        return os.path.getsize(str(self.path))


    def open(self, mode):
        return open(str(self.path), mode)


    def touch(self):
        with open(str(self.path), 'a') as fh:
            pass


    @property
    def md5(self):
        hasher _ hashlib.md5()
        with open(str(self.path), 'rb') as fh:
            data _ fh.read(4096)
            hasher.update(data)

            while data:
                data _ fh.read(4096)
                hasher.update(data)

        return hasher.hexdigest()


    def unlink(self):
        os.unlink(str(self.path))


    @property
    def parent(self):
        return self.FILE_OBJ_FACTORY(self.path.parent)


