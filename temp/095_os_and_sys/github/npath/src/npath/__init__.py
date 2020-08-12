from .Path ______ Path

from .FileObject ______ FileObject
from .File ______ File
from .Directory ______ Directory
from .InvalidFileObject ______ InvalidFileObject

___ file_object_factory(creator, *path_parts):

    if len(path_parts) == 1 and path_parts[0].__class__ is Path:
        path _ path_parts[0]
    else:
        path _ Path(*path_parts)

    if path.is_file:
        return File(path)
    elif path.is_dir:
        return Directory(path)
    else:
        return InvalidFileObject(path)

FileObject.FILE_OBJ_FACTORY _ file_object_factory