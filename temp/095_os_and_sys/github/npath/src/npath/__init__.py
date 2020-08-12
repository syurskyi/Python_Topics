____ .Path ______ Path

____ .FileObject ______ FileObject
____ .File ______ File
____ .Directory ______ Directory
____ .InvalidFileObject ______ InvalidFileObject

___ file_object_factory(creator, *path_parts):

    __ len(path_parts) __ 1 and path_parts[0].__class__ is Path:
        path _ path_parts[0]
    else:
        path _ Path(*path_parts)

    __ path.is_file:
        r_ File(path)
    elif path.is_dir:
        r_ Directory(path)
    else:
        r_ InvalidFileObject(path)

FileObject.FILE_OBJ_FACTORY _ file_object_factory