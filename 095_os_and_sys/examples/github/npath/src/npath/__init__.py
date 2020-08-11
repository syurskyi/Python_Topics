from .Path import Path

from .FileObject import FileObject
from .File import File
from .Directory import Directory
from .InvalidFileObject import InvalidFileObject

def file_object_factory(creator, *path_parts):

    if len(path_parts) == 1 and path_parts[0].__class__ is Path:
        path = path_parts[0]
    else:
        path = Path(*path_parts)

    if path.is_file:
        return File(path)
    elif path.is_dir:
        return Directory(path)
    else:
        return InvalidFileObject(path)

FileObject.FILE_OBJ_FACTORY = file_object_factory