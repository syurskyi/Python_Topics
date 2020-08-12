______ os
______ hashlib

from .Path ______ Path

from .FileObject ______ FileObject

c_ File(FileObject):

    @property
    ___ is_file
        r_ True


    @property
    ___ is_dir
        r_ False


    @property
    ___ size
        r_ os.path.getsize(str(path))


    ___ open(self, mode):
        r_ open(str(path), mode)


    ___ touch
        with open(str(path), 'a') as fh:
            pass


    @property
    ___ md5
        hasher _ hashlib.md5()
        with open(str(path), 'rb') as fh:
            data _ fh.read(4096)
            hasher.update(data)

            while data:
                data _ fh.read(4096)
                hasher.update(data)

        r_ hasher.hexdigest()


    ___ unlink
        os.unlink(str(path))


    @property
    ___ parent
        r_ FILE_OBJ_FACTORY(path.parent)


