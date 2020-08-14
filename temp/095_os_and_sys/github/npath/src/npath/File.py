______ __
______ hashlib

____ .Path ______ Path

____ .FileObject ______ FileObject

c_ File(FileObject):

    ??
    ___ is_file
        r_ T..


    ??
    ___ is_dir
        r_ F..


    ??
    ___ size
        r_ __.path.getsize(str(path))


    ___ o..(, mode):
        r_ o..(str(path), mode)


    ___ touch
        with o..(str(path), 'a') __ fh:
            p..


    ??
    ___ md5
        hasher _ hashlib.md5()
        with o..(str(path), 'rb') __ fh:
            data _ fh.read(4096)
            hasher.update(data)

            while data:
                data _ fh.read(4096)
                hasher.update(data)

        r_ hasher.hexdigest()


    ___ unlink
        __.unlink(str(path))


    ??
    ___ parent
        r_ FILE_OBJ_FACTORY(path.parent)


