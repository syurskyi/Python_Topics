______ __
______ hashlib

____ .Path ______ Path

____ .FileObject ______ FileObject

c_ File(FileObject):

    @property
    ___ is_file
        r_ True


    @property
    ___ is_dir
        r_ False


    @property
    ___ size
        r_ __.path.getsize(str(path))


    ___ open(self, mode):
        r_ open(str(path), mode)


    ___ touch
        with open(str(path), 'a') __ fh:
            pass


    @property
    ___ md5
        hasher _ hashlib.md5()
        with open(str(path), 'rb') __ fh:
            data _ fh.read(4096)
            hasher.update(data)

            while data:
                data _ fh.read(4096)
                hasher.update(data)

        r_ hasher.hexdigest()


    ___ unlink
        __.unlink(str(path))


    @property
    ___ parent
        r_ FILE_OBJ_FACTORY(path.parent)


